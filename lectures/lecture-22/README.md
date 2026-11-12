# Lecture 22 - SQL revision with DuckDB

Back in Lecture 02 you voted for a SQL revision instead of a Polars class, so this is the session you asked for. We write about thirty queries together against the WDI panel you built in Module 06, starting from `SELECT` and ending with window functions and joins. The engine is DuckDB, which needs one import and no server, and every table on the slides is real output from a real run.

[View the slides](https://danilofreire.github.io/datasci350/lectures/lecture-22/22-sql-revision.html)

## What we cover

- Why SQL is declarative, and why the four core clauses look the same in DuckDB, SQLite, PostgreSQL, BigQuery and Snowflake
- DuckDB with no setup: a Parquet path straight in the `FROM` clause, `CREATE VIEW` so the later queries stay short, and `DESCRIBE` and `SUMMARIZE` before you trust a column
- `SELECT`, aliases, `ORDER BY`, `LIMIT`, then `WHERE` with `AND`, `OR`, `NOT`, `IN`, `BETWEEN`, `LIKE` and `ILIKE`
- The order a query runs in, and why an aggregate cannot sit in `WHERE`
- `GROUP BY` and `HAVING`, the five aggregates, and `COUNT(*)` against `COUNT(value)` as a missing-data report you write in one line
- NULLs with `IS NULL` and `COALESCE`, and income bands with `CASE`
- Two window slides: a group mean on every row with `AVG ... OVER (PARTITION BY year)`, and a position with `RANK()`
- Primary keys, foreign keys, and `INNER`, `LEFT` and `FULL OUTER JOIN` on two tiny tables
- DuckDB and pandas: querying a DataFrame by its variable name, and handing the result back with `.df()`
- Two activities we do together: fix a broken query, and predict how many rows three joins return. A join exercise to practise at home, and ten appendices: the exercise's solution, a GROUP BY question to practise at home, grouping by two columns, anti-joins and `UNION`, the three joins side by side, when SQL beats a DataFrame, the same SQL on 200 million rows, timed against pandas and Dask, with its query, and the answers to both activities

## The data

The slides read the small WDI panel from `lectures/lecture-19/data/wdi_panel.parquet`. The 200 million row benchmark reads `data/wdi_big.parquet`, which is about 1.4 GB and is not committed. Rebuild it with:

```bash
cd lectures/lecture-22/data
python make_big_parquet.py
```

The timings themselves were measured once and saved to `data/benchmark_results.csv`, so the deck reads that file rather than re-running anything.

## Rendering

The deck runs every query while it renders, so use a Python that has `duckdb` 1.5.5, `pandas` 3.0.3, `pyarrow` and `yaml`:

```bash
cd lectures/lecture-22
QUARTO_PYTHON=~/miniconda3/envs/datasci/bin/python quarto render 22-sql-revision.qmd
```

## Before the next class

Try the join exercise in the appendix. Work through Tutorial 04, the DuckDB SQL tutorial on the course website. Check that `import duckdb` works in your environment. Lecture 23 moves from making your analysis fast to making it run anywhere, with containers and dependency management.

The previous deck, `22-scaling-in-practice.qmd`, is archived in `lectures/archive/`. Polars now lives in Tutorial 07 on the course website.

Tool claims (DuckDB 1.5.5, and every query re-run on DuckDB 2.0.0) checked on 11 November 2026.
