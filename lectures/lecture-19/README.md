# Lecture 19 - Working with APIs in Practice

Last class one request returned one answer from one keyless API. Real data rarely arrives that politely. This class the server wants to know who is asking, the answer comes back in 35 pages, and the JSON has dictionaries inside dictionaries. By the end you will have written `get_wdi()`, a single function that authenticates, paginates, flattens, cleans, and saves. That function is the first half of your final project's pipeline.

[View the slides](https://danilofreire.github.io/datasci350/lectures/lecture-19/19-apis-in-practice.html)

## What we cover

- Why API keys exist, and why a free key is still a key
- Query string or header, and why headers win: URLs get logged everywhere
- `.env`, `.gitignore`, `.env.example`, and revoking a key the minute it leaks
- Reading the metadata block to know how many pages exist and when to stop
- The page-number loop, and the cursor pagination you will meet elsewhere
- Rate limits: sleeping, exponential backoff, and what a `429` is asking of you
- `pd.json_normalize` on flat records, nested dicts, and nested lists via `record_path` and `meta`
- Cleaning afterwards: renaming, fixing dtypes, and coercing numerics with `errors="coerce"`
- Wrapping the whole pull into `get_wdi()`, with the error check that catches a `200` carrying an apology
- Caching to disk, and parquet against CSV measured on a real 59,024-row panel
- The final project pipeline and the starter repository you clone before next class
- Three exercises, each with a worked solution in the appendix

## Data snapshots

Everything the slides print came from a real request, captured once and saved in `data/`.

- `nasa_apod.json`: NASA's Astronomy Picture of the Day for 5 August 2026, fetched with `DEMO_KEY`
- `wb_gdppc_2023_page1.json`, `page2`, `page3`: GDP per capita for 2023 at `per_page=100`, the three pages the pagination loop walks
- `wb_life_expectancy_5.json`: life expectancy for Brazil, the United States, India, Nigeria, and Japan, 2000 to 2024, 125 records
- `wdi_panel.parquet`: eight indicators for 217 countries, 1990 to 2023, 59,024 rows, built by `data/build_wdi_panel.py`

All of them were pulled on 21 and 22 August 2026. The deck reads them from disk and renders with no network connection, so the numbers on the slides stay put.

## Rendering

```bash
quarto render 19-apis-in-practice.qmd
```

No code executes at render time. Every output on the slides was captured from a real request and pasted in.

## Before the next class

1. Email me your group's names by Thursday 5 November, or I assign you a group at random.
2. Clone the [starter repository](https://github.com/danilofreire/datasci350-project-starter) and run `python scripts/pull_data.py` once.
3. Try the unemployment exercise in Appendix 03.
4. Revise Lectures 12, 14, 15, 16 and 17 for Quiz 03 on Thursday 5 November
5. Optional: the web-scraping tutorial (`tutorials/05-web-scraping-tutorial.qmd`), for when the data sits on a page and there is no API

API claims last verified: 22 August 2026 (NASA DEMO_KEY limits are per IP; World Bank per_page ceiling 32767).

## Using AI in this course

You may use AI for the assignments in this course. Cite the tool you used, check everything it gives you, and remember that the fluency of an answer tells you nothing about whether it is correct.

Using AI tools in a manner prohibited in this course syllabus constitutes Cheating under the Emory Honour Code and is thus a form of academic misconduct.
