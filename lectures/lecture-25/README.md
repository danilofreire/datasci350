# Lecture 25 - Docker for Data Science

Your project is marked from a fresh clone, on a machine with none of the packages you happened to install. This lecture takes the starter's `Dockerfile` apart block by block, so four commands on the marker's laptop give back your report.

[View the slides](https://danilofreire.github.io/datasci350/lectures/lecture-25/25-docker.html)

## What we cover

- The marker's test: four commands from a fresh clone, worth 30% of the project grade
- The starter repository: a pull script, a committed data snapshot, `report.qmd`, `requirements.txt`, and the `Dockerfile`
- The Dockerfile's seven blocks: base image, build settings, apt packages, Quarto, the virtual environment, your files, and the `CMD`
- `.dockerignore`, which took the build context from 1.42MB to 59.36kB
- Layer caching: 7 minutes cold, 0.837 seconds after a title edit, because `COPY requirements.txt` sits above `COPY . /project`
- The `-v` mount. Forget it and the render succeeds, then the report dies with the container
- Two real failures: an uncommitted snapshot that builds fine and fails at run time, and `polars==1.43.9`, a pin that stops the build at step `[6/8]`
- `docker system df` and `prune`, then Compose, ready-made images, and pushing to Docker Hub

## The demo

The demo is the [project starter](https://github.com/danilofreire/datasci350-project-starter) itself, the repository your group works in. `demo/README.md` has the build and run commands, a `compose.yaml` to write yourself, the pandas exercise, and the two failures to reproduce on purpose.

## Rendering

```bash
quarto render 25-docker.qmd
```

Nothing on the slides executes; every output is pre-captured.

## Before the next class

No class on 26 November. Lecture 26, on 1 December, is revision: bring your repository and your questions. Quiz 05, on 3 December, covers Lectures 21, 22, 23, and 25. The final project is due on 8 December.

1. Clone your own repository into a new, empty folder and run the four commands from the marking slide.
2. Run `git ls-files data/raw`. It should print two file names.
3. Run `git shortlog -sn`. Every group member should appear.

## Verification

Built and captured on 26 August 2026: Docker 29.4.0 (through OrbStack), Docker Compose v5.1.2, Quarto 1.9.37 inside the image (1.9.38 on the laptop), Ubuntu 24.04, Python 3.12.3, starter commit 7d79f5b plus the .dockerignore fix. Cold build 7 min, cached rebuild 0.8 s. Screenshots of Docker Hub, Jupyter Docker Stacks, rocker, and the starter repository taken the same day.

## Using AI in this course

You may use AI for the assignments in this course. Cite the tool you used, check everything it gives you, and remember that the fluency of an answer tells you nothing about whether it is correct.

Using AI tools in a manner prohibited in this course syllabus constitutes Cheating under the Emory Honour Code and is thus a form of academic misconduct.
