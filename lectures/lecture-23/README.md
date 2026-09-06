# Lecture 23 - Dependency Management, Virtual Environments, and Containers

Your pipeline works on your laptop, with the packages you happened to install. This lecture is about closing the gap between that and a stranger who runs one command and gets your results back.

[View the slides](https://danilofreire.github.io/datasci350/lectures/lecture-23/23-containers.html)

## What we cover

- Why working code breaks: the Python 2 `print` statement against Python 3, with the real traceback
- `venv` and `pip freeze`: an isolated Python, and a `requirements.txt` of `==` pins that installs the same versions elsewhere
- Conda in one slide: `conda env export --from-history`, and the build strings that make a full export unportable
- `uv`: `uv init`, `uv add`, `uv sync`, and `uv export` for handing a project to a Dockerfile
- Images, containers, and registries, plus Docker Desktop's licence: free under 250 employees and $10M revenue, with Podman, Colima, OrbStack, and Rancher Desktop as free alternatives
- Building, caching, pushing, and pulling `datasci350-example`

## The demo folder

`docker/` holds the three files built on the slides; `docker/README.md` has the build and run instructions. The exercise asks you to add `polars==1.44.0`, rebuild, and read which layers say `CACHED`.

## Rendering

```bash
quarto render 23-containers.qmd
```

Nothing on the slides executes; every output is pre-captured.

## Before the next class

Quiz 04 is on 19 November. It covers web APIs and JSON from Lectures 18 and 19, with no new material.

Lecture 25, on 24 November, builds the project container in class. Before that class:

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop) or a free alternative, and check that `docker run hello-world` works.
2. Create a free account on [Docker Hub](https://hub.docker.com/).
3. Clone the [project starter](https://github.com/danilofreire/datasci350-project-starter) and run `docker build` once. It downloads a lot, so do it on your own wifi.

The final project is due on 8 December. Quiz 05, on 3 December, covers Lectures 21, 22, 23, and 25.

## Verification

Tool versions and every terminal output verified on 25 August 2026: Python 3.14, uv 0.11.7, conda 26.1.1, Docker 29.4.0 (through OrbStack), NumPy 2.5.2, pandas 3.0.5, Polars 1.44.0. Docker Hub's Data Science category held 9,427 images and the Docker Desktop licence thresholds were read from docker.com/pricing/faq on the same date. The Docker Hub push and its screenshot were refreshed on 26 August 2026.

## Using AI in this course

You may use AI for the assignments in this course. Cite the tool you used, check everything it gives you, and remember that the fluency of an answer tells you nothing about whether it is correct.

Using AI tools in a manner prohibited in this course syllabus constitutes Cheating under the Emory Honour Code and is thus a form of academic misconduct.
