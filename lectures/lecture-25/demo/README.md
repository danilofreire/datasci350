# Lecture 25 demo

The demo for this lecture is the project starter itself. Clone it and work inside your clone:

```bash
git clone https://github.com/danilofreire/datasci350-project-starter
```

## Build and run

```bash
docker build -t datasci350-project .
docker run --rm -v "$(pwd)/output:/project/output" datasci350-project
```

Open `output/report.html`. Without the `-v` flag the report renders and then disappears with the container.

## Compose (optional)

The starter does not ship a `compose.yaml`. Write one yourself:

```yaml
services:
  report:
    build: .
    image: datasci350-project
    volumes:
      - ./output:/project/output
```

Then run `docker compose up --build`.

## The exercise

Add `pandas==3.0.5` to `requirements.txt`, import it in `report.qmd`, and rebuild. Watch which layers say `CACHED` and which rebuild.

## Break it on purpose

In a scratch clone, add `data/raw/` to `.gitignore` and build from a fresh clone: the render fails because the data is missing. Then set a pin that does not exist, such as `polars==1.43.9`, and rebuild: pip stops the build
