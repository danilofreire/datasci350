"""Build the teaching panel used in Lectures 18, 21 and 22.

Fetches eight World Development Indicators for every country (aggregates such as
"World" and "Euro area" are dropped) for the years 1990-2023, and writes a long
format panel to wdi_panel.parquet.

Run it from this directory:

    python build_wdi_panel.py

Raw API responses are cached alongside this script in raw/, so a second run does
no network requests at all. Delete raw/ to force a fresh download.

Note: raw/ is about 18 MB of intermediate JSON and is not worth committing. Add
`lectures/lecture-18/data/raw/` to .gitignore before committing this folder. The
file that belongs in the repository is wdi_panel.parquet, at roughly 450 KB.

This script is the answer to the question "where did your data come from?".
"""

import json
import time
from pathlib import Path

import pandas as pd
import requests

BASE = "https://api.worldbank.org/v2"
HERE = Path(__file__).parent
RAW = HERE / "raw"

# Indicator code -> short name used in the panel.
# EN.ATM.CO2E.PC, the CO2 code used in older course material, was retired by the
# World Bank and now returns "The indicator was not found". Its successor is the
# Climate Watch series below.
INDICATORS = {
    "NY.GDP.PCAP.KD": "gdp_per_capita",
    "SP.POP.TOTL": "population",
    "SP.DYN.LE00.IN": "life_expectancy",
    "EN.GHG.CO2.PC.CE.AR5": "co2_per_capita",
    "IT.NET.USER.ZS": "internet_users_pct",
    "SP.URB.TOTL.IN.ZS": "urban_pop_pct",
    "SP.DYN.TFRT.IN": "fertility_rate",
    "SE.PRM.NENR": "primary_enrolment_net",
}

START, END = 1990, 2023


def fetch_json(url, params, cache_name):
    """Fetch a URL once, then read from disk forever after."""
    RAW.mkdir(exist_ok=True)
    cached = RAW / cache_name
    if cached.exists():
        with open(cached) as f:
            return json.load(f)

    r = requests.get(url, params=params, timeout=60)
    r.raise_for_status()
    payload = r.json()

    with open(cached, "w") as f:
        json.dump(payload, f)
    time.sleep(0.5)  # be a polite guest
    return payload


def real_countries():
    """ISO3 codes of actual countries, excluding regional and income aggregates.

    The World Bank marks aggregates with region id 'NA'.
    """
    payload = fetch_json(f"{BASE}/country", {"format": "json", "per_page": 400}, "countries.json")
    return {c["id"] for c in payload[1] if c["region"]["id"] != "NA"}


def fetch_indicator(code):
    """All countries, all years, for one indicator. One request: per_page is generous."""
    payload = fetch_json(
        f"{BASE}/country/all/indicator/{code}",
        {"format": "json", "date": f"{START}:{END}", "per_page": 20000},
        f"{code}.json",
    )

    if isinstance(payload, dict) or payload[1] is None:
        raise RuntimeError(f"{code} returned no data. Has it been retired?")

    meta = payload[0]
    if meta["pages"] > 1:
        raise RuntimeError(f"{code} needs pagination: {meta['pages']} pages")

    return payload[1]


def main():
    keep = real_countries()
    print(f"{len(keep)} countries after dropping aggregates")

    frames = []
    for code, name in INDICATORS.items():
        records = fetch_indicator(code)
        df = pd.json_normalize(records)
        df = df[df["countryiso3code"].isin(keep)]
        df = pd.DataFrame(
            {
                "country": df["country.value"],
                "iso3": df["countryiso3code"],
                "indicator": name,
                "year": df["date"].astype("int16"),
                "value": pd.to_numeric(df["value"], errors="coerce"),
            }
        )
        frames.append(df)
        print(f"  {code:<24} {name:<22} {len(df):>7,} rows, {df['value'].notna().sum():>7,} non-missing")

    panel = pd.concat(frames, ignore_index=True)
    panel = panel.sort_values(["iso3", "indicator", "year"]).reset_index(drop=True)
    panel["country"] = panel["country"].astype("category")
    panel["iso3"] = panel["iso3"].astype("category")
    panel["indicator"] = panel["indicator"].astype("category")

    out = HERE / "wdi_panel.parquet"
    panel.to_parquet(out, index=False, compression="snappy")

    print(f"\nwrote {out.name}: {len(panel):,} rows, {out.stat().st_size / 1024:.0f} KB")
    print(f"  countries:  {panel['iso3'].nunique()}")
    print(f"  indicators: {panel['indicator'].nunique()}")
    print(f"  years:      {panel['year'].min()}-{panel['year'].max()}")


if __name__ == "__main__":
    main()
