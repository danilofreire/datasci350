# Lecture 23 demo container

Three files: a `Dockerfile`, a pinned `requirements.txt`, and a `hello.py` that prints the NumPy and pandas versions from inside the image.

## Build it

Open a terminal in this folder.

```bash
docker build -t datasci350-example .
```

The first build downloads the `python:3.14-slim` base image and installs the packages. Later builds reuse the cached layers.

## Run it

```bash
docker run --rm datasci350-example
```

Expected output:

```
Hello, DATASCI350!
numpy  2.5.2
pandas 3.0.5
```

`--rm` deletes the container when it exits.

## The exercise

Add `polars==1.44.0` to `requirements.txt`, import `polars` in `hello.py`, and print `pl.__version__`. Rebuild and read which steps say `CACHED`. The solution is in Appendix 01 of the slides.
