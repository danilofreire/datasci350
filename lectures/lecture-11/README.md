# Lecture 11 - Quarto in Practice

Everything Quarto builds once you know the basics: articles with citations, PDFs, slides, websites, and one report that becomes ten.

[View the slides](https://danilofreire.github.io/datasci350/lectures/lecture-11/11-more-quarto.html)

## What we cover

- Markdown beyond the basics: tables, footnotes, and maths
- Rendering existing Jupyter notebooks without rewriting them
- PDFs through LaTeX, and citations from a `.bib` file
- Cross-references: label a figure `fig-rain`, write `@fig-rain`, get "Figure 1"
- `freeze`, so that rendering a document does not quietly recompute your results
- Slides with reveal.js, and websites with `quarto publish gh-pages`
- Parameterised reports, and the shell loop that turns one report into ten

## The two exercises

The first asks for a `practice.qmd` with a labelled figure, a cross-reference, and one citation, rendered to HTML and PDF.

The second needs no writing. Download [`report.qmd`](report.qmd) and [`country_profiles.csv`](data/country_profiles.csv), put the CSV in a `data` folder beside the report, and drive the same file from the terminal:

```bash
quarto render report.qmd
quarto render report.qmd -P country:Japan --output profile-Japan.html
```

The first gives you Brazil, the default in the tagged cell. The second gives you Japan without editing a line. Solutions are in the appendix slides.

## When something breaks

Python errors read from the bottom, YAML errors from the top. In a LaTeX error, `l.172` counts lines in the generated `.tex` file, not in your `.qmd`.

A `ModuleNotFoundError` for a package you installed means Quarto is running a different Python. Run `quarto check jupyter` and compare it with `which python3`. Note that `QUARTO_PYTHON` overrides an activated environment.

## Before the next class

1. Complete both exercises.
2. Publish something with `quarto publish gh-pages`. One page is enough.
3. Fix any render that failed today.

### Install Ollama at home

Next class you run a language model on your own laptop, which needs a 1.3 GB download that classroom wifi cannot deliver twenty-five times at once.

1. Download Ollama from <https://ollama.com/download> and install it.
2. Open a **new** terminal window and run `ollama --version`.
3. Run `ollama pull llama3.2:1b`.
4. Run `ollama run llama3.2:1b`, ask it anything, then type `/bye`.

If step 2 says `command not found`, close the terminal and open a new one. If your laptop cannot run the model, tell me before class and we will arrange a lab machine.
