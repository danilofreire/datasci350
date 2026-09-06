# Lecture 10 - Reproducible Research and Literate Programming

Why so much published research falls apart when someone tries to re-run it, what to do differently, and the tool we will use for the rest of the course.

[View the slides](https://danilofreire.github.io/datasci350/lectures/lecture-10/10-quarto.html)

## What we cover

- The reproducibility crisis, and why most computational results fail for a mundane reason: the code does not run
- The ladder: re-runnable, reproducible, replicable, reusable. This course gets you to the second step
- The four ingredients that must travel together: code, data, environment, documentation
- Project structure, and why `data/raw/` is read-only
- Cleaning data with code rather than by hand
- Relative paths, random seeds, and recording your package versions
- Literate programming: text, code, and results in one file
- Quarto: installing it, the YAML header, code chunks, and your first document

## Two stories worth remembering

**Reinhart and Rogoff (2010)** concluded that growth turns negative above 90% debt-to-GDP, and the paper became the standard citation for austerity after the 2008 crisis. In 2013 a graduate student could not reproduce it. One spreadsheet formula averaged rows 30 to 44 instead of 30 to 49, dropping five countries. Corrected, growth above the threshold was +2.2%, not -0.1%.

**Trisovic et al. (2022)** downloaded 2,109 R files from Harvard Dataverse and tried to run them. 74% failed on the first attempt. These were files authors chose to deposit alongside their publications.

## The habits, in one list

1. Never edit raw data by hand. Write a cleaning script instead.
2. Never write an absolute path. If your code contains your username, it is not reproducible.
3. Set a seed for anything random.
4. Write down your Python and package versions.
5. Keep a README that says what the project is and how to rebuild it.

## Practice

The exercise asks you to build a `weather.qmd` from scratch: a YAML header, a heading, a table, and a bar chart with its code hidden. The solution is in the appendix slide.

If Quarto misbehaves, `quarto check` diagnoses the installation before you start debugging your document.

## Before the next class

1. Install Quarto from [quarto.org/docs/download](https://quarto.org/docs/download/).
2. Run `quarto check` and make sure it passes.
3. Install the Quarto extension for VS Code.
4. Complete the exercise. It is the real installation test.

Next time we go further with Quarto: Markdown in depth, PDFs and citations, `freeze` for renders you can trust, presentations and websites, and parameterised reports that write one document per country.
