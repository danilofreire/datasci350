# Lecture 10 - Reproducible Research and Literate Programming

Why so much published research falls apart when someone tries to re-run it, what to do differently, and the tool we will use for the rest of the course.

[View the slides](https://danilofreire.github.io/datasci350/lectures/lecture-10/10-quarto.html)

## What we cover

- The reproducibility crisis, and why most computational results fail for a mundane reason: the code does not run
- The ladder: re-runnable, reproducible, replicable, reusable. This course gets you to the second step
- The four ingredients that must travel together: code, data, environment, documentation
- Project structure, and why `data/raw/` is read-only
- Relative paths, random seeds, and recording your package versions
- Literate programming: text, code, and results in one file
- Quarto: installing it, the YAML header, code chunks, and your first document

## Two stories worth remembering

Reinhart and Rogoff (2010) found that growth turns negative above 90% debt-to-GDP, and the paper became the standard citation for austerity. In 2013 a graduate student could not reproduce it: one spreadsheet formula averaged rows 30 to 44 instead of 30 to 49. Corrected, growth was +2.2%, not -0.1%.

Trisovic et al. (2022) tried to run 2,109 R files from Harvard Dataverse. 74% failed on the first attempt.

## The habits

Never edit raw data by hand. Never write an absolute path. Set a seed for anything random. Write down your package versions. Keep a README that says how to rebuild the project.

## Practice

Build a `weather.qmd` from scratch: YAML header, heading, table, and a bar chart with its code hidden. The solution is in the appendix slide. If Quarto misbehaves, `quarto check` diagnoses the installation first.

## Before the next class

1. Install Quarto from [quarto.org/docs/download](https://quarto.org/docs/download/).
2. Run `quarto check` and make sure it passes.
3. Install the Quarto extension for VS Code.
4. Complete the exercise. It is the real installation test.

Next time: Markdown in depth, PDFs and citations, `freeze`, websites, and parameterised reports.
