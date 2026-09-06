# Lecture 22 - SQL revision with DuckDB

Back in Lecture 02 you voted for a SQL revision instead of a Polars class, so this is the session you asked for. We write about thirty queries together against the WDI panel you built in Module 06, starting from `SELECT` and ending with window functions and joins. The engine is DuckDB, which needs one import and no server, and every table on the slides is real output from a real run. The last section repeats the same queries in plain `sqlite3`, because that is what assignment 09 uses.

[View the slides](https://danilofreire.github.io/datasci350/lectures/lecture-22/22-sql-revision.html)

## What we cover

- Why SQL is declarative, and why the four core clauses look the same in DuckDB, SQLite, PostgreSQL, BigQuery and Snowflake
- DuckDB with no setup: a Parquet path straight in the `FROM` clause, `CREATE VIEW` so the later queries stay short, and `DESCRIBE` and `SUMMARIZE` before you trust a column
- `SELECT`, aliases, `ORDER BY`, `LIMIT`, then `WHERE` with `AND`, `OR`, `NOT`, `IN`, `BETWEEN`, `LIKE` and `ILIKE`
- The order a query really runs in, and why an aggregate cannot sit in `WHERE`
- `GROUP BY` and `HAVING`, the five aggregates, and `COUNT(*)` against `COUNT(value)` as a missing-data report you write in one line
- NULLs with `IS NULL` and `COALESCE`, income bands with `CASE`, and a window function beside a `GROUP BY`
- Primary keys, foreign keys, and `INNER`, `LEFT` and `FULL OUTER JOIN` on two tiny tables
- SQL in Python: querying a pandas DataFrame by its variable name, handing the result back with `.df()`, and the same queries in `sqlite3` with a connection, cursor, `commit()` and `fetchall()`
- The four places DuckDB and SQLite differ, and the same SQL on 200 million rows timed against pandas and Dask
- Two exercises with worked solutions, and eight appendices: grouping by two columns, anti-joins and `UNION`, when SQL beats a DataFrame, the benchmark query, the full `sqlite3` listing, and the errors you are most likely to hit

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

Finish both exercises if you did not complete them in class. Start assignment 09, which asks you to join two tables in SQLite. Check that `import duckdb` and `import sqlite3` both work in your environment. Lecture 23 moves from making your analysis fast to making it run anywhere, with containers and dependency management.

The previous deck, `22-scaling-in-practice.qmd`, is still in this folder. Polars now lives in Tutorial 07 on the course website.

Tool claims (DuckDB 1.5.5, SQLite 3.53) checked on 2 September 2026.
