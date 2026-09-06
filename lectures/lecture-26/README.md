# Lecture 26 - Revision: Scaling, SQL and Containers

The last class before Quiz 05. We revise the four lectures the quiz covers, write four SQL queries together on the World Bank panel, and spend the end of the class on your project containers.

[View the slides](https://danilofreire.github.io/datasci350/lectures/lecture-26/26-revision.html)

## What we cover

- Scaling and performance (Lecture 21): `map` and embarrassingly parallel work, `joblib` against `concurrent.futures`, Big O, Amdahl's law with the arithmetic on the slide, the GIL, Dask and lazy evaluation, and the 200-million-row benchmark
- SQL revision (Lecture 22): the evaluation-order ladder, `WHERE` against `HAVING`, `COUNT(*)` against `COUNT(value)`, the three joins, the `sqlite3` boilerplate, and the two dialect traps
- SQL practice: four exercises of rising difficulty on `lectures/lecture-19/data/wdi_panel.parquet`, about twenty-five minutes of class time
- Containers (Lecture 23): why working code breaks, `venv` and `pip` against conda against `uv`, and images, containers and registries
- Docker (Lecture 25): the project Dockerfile block by block, layer caching, `-v` and `-p`, and the checklist the marker's machine works from
- Quiz 05 preparation: the kind of question each lecture brings, and a revision plan
- Project Q&A: the three failures I expect, and where the answers live

## The exercises

| Exercise | What it practises | Solution |
| --- | --- | --- |
| 01 | `WHERE`, an alias, `ORDER BY DESC`, `LIMIT` | Appendix 01 |
| 02 | `GROUP BY` with `HAVING`, and the two `COUNT`s | Appendix 02 |
| 03 | `LEFT JOIN` with a small `regions` table, and the `COUNT(*)` trap | Appendix 03 |
| 04 | The same query under `sqlite3`, with a `?` placeholder | Appendix 04 |

Every solution runs when the deck is rendered, so the tables in the appendices are real output from the panel.

## Rendering

```bash
QUARTO_PYTHON=~/miniconda3/envs/datasci/bin/python quarto render 26-revision.qmd
```

The deck needs `duckdb` and `pandas`, and it reads `../lecture-19/data/wdi_panel.parquet`. Nothing calls the network.

## Before the next class

Quiz 05 is on Thursday 3 December and covers Lectures 21, 22, 23 and 25.

The final project is due on Tuesday 8 December at 11:59pm, on Canvas, and it must render inside a container. Test yours from a fresh clone before then. Appendix 05 lists the commands I run on your repository.

## Verification

Content aligned with the Fall 2026 decks for Lectures 21, 22, 23 and 25 on 2 September 2026. Query outputs produced with DuckDB 1.5.5, SQLite 3.53.1 and pandas 3.0.3.

## Using AI in this course

You may use AI for the assignments in this course. Cite the tool you used, check everything it gives you, and remember that the fluency of an answer tells you nothing about whether it is correct.

Using AI tools in a manner prohibited in this course syllabus constitutes Cheating under the Emory Honour Code and is thus a form of academic misconduct.
