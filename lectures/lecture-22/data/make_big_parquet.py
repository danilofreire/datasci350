"""Generate the large synthetic panel used in the Lecture 22 benchmark.

The teaching panel from Lecture 19 (lectures/lecture-19/data/wdi_panel.parquet)
holds about 59,000 rows, which every tool on your laptop handles instantly. That
is useless for a benchmark. This script inflates it to roughly 200 million rows
by cloning each country into many synthetic entities and jittering the values.

The result is NOT committed to the repository: it is around 1.5 GB, and it is
fully reproducible from this script plus the small panel. That is the trade we
teach in Module 06, applied to ourselves.

Usage
-----
    python make_big_parquet.py                 # ~200M rows, the default
    python make_big_parquet.py --replicas 400  # smaller, for a slower laptop
    python make_big_parquet.py --help

Expect a few minutes and roughly 2 GB of free disk. Memory use stays near
constant: rows are written in row groups as they are generated, never held all
at once.
"""

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

HERE = Path(__file__).parent
SOURCE = HERE.parent.parent / "lecture-19" / "data" / "wdi_panel.parquet"
OUTPUT = HERE / "wdi_big.parquet"

# One replica of the source panel is ~59,000 rows, so 3,400 replicas is ~200M.
DEFAULT_REPLICAS = 3_400

# Fixed seed: two people running this script get the same file.
SEED = 350


def build_arrow_schema():
    """Plain (non-dictionary) types keep the writer simple and the file portable."""
    return pa.schema(
        [
            ("country", pa.string()),
            ("iso3", pa.string()),
            ("entity", pa.string()),
            ("indicator", pa.string()),
            ("year", pa.int16()),
            ("value", pa.float64()),
        ]
    )


def make_replica(base, replica_id, rng):
    """One synthetic copy of the panel.

    Each country becomes a distinct entity (BRA_0001, BRA_0002, ...) and every
    value is multiplied by a small random factor, so the numbers differ but the
    distributions and the missing-value pattern stay realistic.
    """
    n = len(base)
    jitter = rng.normal(loc=1.0, scale=0.05, size=n)

    return pd.DataFrame(
        {
            "country": base["country"].astype(str).to_numpy(),
            "iso3": base["iso3"].astype(str).to_numpy(),
            "entity": base["iso3"].astype(str).to_numpy() + f"_{replica_id:04d}",
            "indicator": base["indicator"].astype(str).to_numpy(),
            "year": base["year"].to_numpy(),
            "value": base["value"].to_numpy() * jitter,
        }
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--replicas", type=int, default=DEFAULT_REPLICAS,
                        help=f"how many synthetic copies of the panel (default {DEFAULT_REPLICAS})")
    parser.add_argument("--output", type=Path, default=OUTPUT, help="where to write the parquet file")
    parser.add_argument("--batch", type=int, default=20,
                        help="replicas per row group; lower this if memory is tight (default 20)")
    args = parser.parse_args()

    if not SOURCE.exists():
        raise SystemExit(
            f"Cannot find {SOURCE}.\n"
            "Build the teaching panel first: run build_wdi_panel.py in lectures/lecture-19/data/"
        )

    base = pd.read_parquet(SOURCE)
    rng = np.random.default_rng(SEED)
    schema = build_arrow_schema()

    rows_per_replica = len(base)
    target = rows_per_replica * args.replicas
    print(f"source panel:  {rows_per_replica:,} rows")
    print(f"replicas:      {args.replicas:,}")
    print(f"target:        {target:,} rows")
    print(f"writing to:    {args.output}\n")

    written = 0
    with pq.ParquetWriter(args.output, schema, compression="snappy") as writer:
        for start in range(0, args.replicas, args.batch):
            stop = min(start + args.batch, args.replicas)
            chunk = pd.concat(
                [make_replica(base, i, rng) for i in range(start, stop)],
                ignore_index=True,
            )
            writer.write_table(pa.Table.from_pandas(chunk, schema=schema, preserve_index=False))

            written += len(chunk)
            pct = 100 * written / target
            print(f"  {written:>13,} rows  ({pct:5.1f}%)", end="\r", flush=True)

    size_gb = args.output.stat().st_size / 1024**3
    print(f"\n\ndone: {written:,} rows, {size_gb:.2f} GB")
    print(f"      {args.output}")
    print("\nThis file is gitignored. Anyone can rebuild it by running this script.")


if __name__ == "__main__":
    main()
