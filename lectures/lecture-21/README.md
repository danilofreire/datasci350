# Lecture 21 - Parallel computing fundamentals

Your laptop has eight cores and your Python script uses one of them. This lecture is about the other seven, and about the more useful question underneath: whether you need them at all. We time a slow function four ways, watch a parallel version lose to a serial one, and work out why. Then we meet Dask, which splits both the work and the data, and read its dashboard while it runs.

[View the slides](https://danilofreire.github.io/datasci350/lectures/lecture-21/21-parallel-computing.html)

## What we cover

- Serial execution, the `map` function, and which problems are embarrassingly parallel
- `joblib` with `Parallel` and `delayed`, timed against the serial version
- `concurrent.futures`: `ProcessPoolExecutor` for CPU work, `ThreadPoolExecutor` for waiting
- Big O notation, and why four cores cannot rescue an O(n²) algorithm
- Amdahl's law: the serial share caps your speed-up
- The Global Interpreter Lock and why threads do not always help
- Dask arrays and DataFrames, lazy evaluation, and `.compute()`
- Reading and writing CSV and parquet with Dask, with real timings
- `dask.delayed` for pipelines, the task graph, and the dashboard at `localhost:8787`
- Best practices: what to try before you parallelise

Every timing on the slides comes from a real run on my laptop, including two where the parallel version was slower.

## Rendering

The deck executes its own benchmarks, so a render takes several minutes. Use a Python that has `dask`, `distributed`, `pyarrow`, `graphviz` and `yaml`, and make sure the Graphviz `dot` binary is on the PATH (the task-graph slide needs it). On my machine both live in the `datasci` conda environment, so rendering inside it is simplest:

```bash
conda run -n datasci quarto render 21-parallel-computing.qmd
```

`dask.visualize` also needs the graphviz binary itself, not only the Python package (`brew install graphviz` on macOS, `apt install graphviz` on Linux).

The CSV and parquet files under `data/` are not stored in the repository. The deck generates them from `dask.datasets.timeseries()` while it runs, so run the cells in order: the ones that read `data/` come after the ones that write it. The generator has no fixed seed, so your numbers will differ from the ones on the slides.

## Before the next class

Run the two exercises. Lecture 22 benchmarks Polars and DuckDB against pandas and Dask on the WDI panel you built in Module 06, so bring your timings.

The serial, `map` and `joblib` material is adapted from [the Yale Center for Research Computing](https://github.com/ycrc/parallel_python), with thanks.

Tool claims and screenshots verified August 2026 (Dask 2026.7.1).
