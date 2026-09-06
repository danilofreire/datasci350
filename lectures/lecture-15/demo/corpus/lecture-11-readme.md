# Lecture 11 - Quarto in Practice

Everything Quarto builds once you know the basics: articles with citations, PDFs, slides, websites, and one report that becomes ten.

[View the slides](https://danilofreire.github.io/datasci350/lectures/lecture-11/11-more-quarto.html)

## What we cover

- Markdown beyond the basics: tables, footnotes, maths, and the bits you will use every week
- Rendering existing Jupyter notebooks without rewriting them
- PDFs through LaTeX, and templates for when a journal wants a particular look
- Citations from a `.bib` file, and where BibTeX entries come from
- Cross-references: label a figure `fig-rain`, write `@fig-rain`, get "Figure 1"
- `freeze`, so that rendering a document does not quietly recompute your results
- Slides with reveal.js, and where to host them
- Websites: a folder, a `_quarto.yml`, and `quarto publish gh-pages`
- Parameterised reports, and the shell loop that turns one report into ten

## The two exercises

The first asks you to write a `practice.qmd` from scratch: a YAML header, a figure with a label, a cross-reference to it, and one citation from a `.bib` file. Render it to HTML and to PDF.

The second needs no writing at all. Download [`report.qmd`](report.qmd) and [`country_profiles.csv`](data/country_profiles.csv), put the CSV in a `data` folder beside the report, and drive the same file from the terminal:

```bash
quarto render report.qmd
quarto render report.qmd -P country:Japan --output profile-Japan.html
```

The first command gives you Brazil, because that is the default in the tagged cell. The second gives you Japan without editing a single line. Solutions to both exercises are in the appendix slides.

## What freeze is for

`freeze: auto` tells Quarto to re-run a document only when that document's source changes. Without it, every render recomputes everything, so a typo fix in November can change your results because a package was updated in October.

Commit the `_freeze/` folder. It travels with the project, so whoever clones your repository gets your numbers rather than their own.

`freeze` controls when your code runs, not what it runs with. Pinning the packages themselves is module 08.

## When the render fails

Python errors read from the bottom. The last line names the problem, and Quarto tells you which cell broke.

YAML errors read from the top. Trust the caret: it points at the character that broke the header, and the stack trace underneath is noise.

In a LaTeX error, `l.172` counts lines in the generated `.tex` file, not in your `.qmd`. The text printed beside it is yours, so search your file for that instead.

## When Quarto uses the wrong Python

A `ModuleNotFoundError` for a package you know you installed means Quarto is running a different Python from the one you installed it into. Run `quarto check jupyter` to see which one it is, and compare it with `which python3`.

Warning: `QUARTO_PYTHON` overrides an activated environment. If that variable is set in your shell profile, option 1 below will not work until you unset it.

1. Activate your environment. Render from that same terminal.
2. Or set the interpreter for one render: `QUARTO_PYTHON=~/.venv/bin/python quarto render report.qmd`.
3. Or register your environment as a Jupyter kernel. Name it in the YAML with `jupyter: ds350`. This is the option that travels with the file, so use it for work you share.

## Before the next class

1. Complete both exercises.
2. Publish something with `quarto publish gh-pages`. One page is enough.
3. Fix any render that failed today. Do not leave it until the week of the final project.

### Install Ollama at home

Next class you run a language model on your own laptop. That needs a 1.3 GB download, which the classroom wifi cannot deliver twenty-five times at once. Do these steps before you arrive.

1. Open <https://ollama.com/download>.
2. Download the installer for your operating system.
3. Install Ollama as you would any other application.
4. Open a new terminal window. An older window will not know where Ollama is.
5. Run `ollama --version`. A version number appears.
6. Run `ollama pull llama3.2:1b`. The download takes a few minutes.
7. Run `ollama run llama3.2:1b`. A `>>>` prompt appears.
8. Ask it any question, then type `/bye` to leave.

If step 5 says `command not found`, close the terminal and open a new one. That fixes it almost every time. If your laptop cannot run the model, tell me before class and we will arrange a lab machine.

Next class we change subject: local language models. A trained model turns out to be a file you can download, and we take one apart, read every setting inside it, and then build a chatbot with a personality of your own choosing.
