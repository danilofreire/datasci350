# DATASCI 350 - Data Science Computing

## Course Description

Welcome to [DATASCI 350](https://github.com/danilofreire/datasci350)! This course
introduces key tools in modern data science, focusing on three essential
aspects: reliability, reproducibility, and robustness. We will cover command
line interfaces, version control with [Git](https://git-scm.com/) and
[GitHub](https://github.com/), and literate programming using
[Quarto](https://quarto.org/) and [Jupyter Notebooks](https://jupyter.org/).
You will also learn about data storage and manipulation with
[SQL](https://www.w3schools.com/sql/) and [Pandas](https://pandas.pydata.org/),
data visualisation using [Matplotlib](https://matplotlib.org/),
[Seaborn](https://seaborn.pydata.org/) and
[plotnine](https://plotnine.readthedocs.io/), and parallel computing with
[Dask](https://www.dask.org/). We will explore artificial intelligence-assisted
programming with [GitHub Copilot](https://github.com/features/copilot) and
finish with [Docker](https://www.docker.com/) and containerisation. Throughout
the course, you will learn how to use these tools to improve your data science
workflow and create more reliable, reproducible, and robust analyses.

## Contact Information

- Instructor: [Danilo Freire](https://danilofreire.github.io/)
  - Email: [`danilofreire@gmail.com`](mailto:danilofreire@gmail.com)
  - Office hours: By appointment at any time (online or in person)

- Teaching Assistants:
  - [Alix Morales](mailto:alix.morales@emory.edu) (in class)
  - [Harris Wang](mailto:harris.wang@emory.edu) (grader)
  - Feel free to email them to arrange a meeting

## Learning Outcomes

By the end of this course, students will be able to:

- Use data science tools for project collaboration and version control
- Collect data from web APIs and web pages, and process it at scale
- Create clear data visualisations and write well-documented code
- Use AI tools to help with programming tasks
- Understand the basics of containerisation and parallel computing

## Repository Structure

This repository is organised as follows:

- [`assignments/`](https://github.com/danilofreire/datasci350/tree/main/assignments): Contains all course assignments
- [`lectures/`](https://github.com/danilofreire/datasci350/tree/main/lectures): Includes lecture materials and code
- [`tutorials/`](https://github.com/danilofreire/datasci350/tree/main/tutorials): Step-by-step guides for the tools used in the course
- [`grades/`](https://github.com/danilofreire/datasci350/tree/main/grades): Reusable Python script for computing final grades from a Canvas CSV export, applying the syllabus weights and 11-band rubric. Student data is excluded from version control via a folder-level `.gitignore`.
- [`README.md`](https://github.com/danilofreire/datasci350/blob/main/README.md): This file, providing an overview of the course and repository
- [`syllabus.pdf`](https://github.com/danilofreire/datasci350/blob/main/syllabus/syllabus.pdf): Course syllabus in PDF format

The course website is available at <https://danilofreire.github.io/datasci350/>.

## Downloading the Repository

The quickest way to download the course materials is a **shallow clone**, which fetches only the current files without the full history of past changes. This keeps the download small and works well on slow connections:

```bash
git clone --depth 1 https://github.com/danilofreire/datasci350.git
```

If you would like the complete history (for example, to see how the materials evolved over the semester), omit the flag:

```bash
git clone https://github.com/danilofreire/datasci350.git
```

The full clone takes longer and uses more disk space, but it is not required for the course.

### Updating Your Copy

When new lectures or fixes are added, pull the latest changes from inside the repository folder:

```bash
cd datasci350
git pull
```

This works the same way on shallow and full clones.

## Getting Help

If you encounter any issues with the course materials or have questions about the content, please:

1. Check the [course syllabus](https://github.com/danilofreire/datasci350/blob/main/syllabus/syllabus.pdf) and this README for relevant information
2. Review the [lecture materials](https://github.com/danilofreire/datasci350/tree/main/lectures) and [tutorials](https://github.com/danilofreire/datasci350/tree/main/tutorials) in the repository
3. Consult with your classmates or post in the [course discussion forum](https://github.com/danilofreire/datasci350/discussions)
4. Schedule an appointment with the instructor

## Contributing to the Repository

While this repository is primarily maintained by the course instructor, everyone is welcome to contribute. Please feel free to suggest improvements or report issues by [opening a GitHub issue](https://github.com/danilofreire/datasci350/issues), [submitting a pull request](https://github.com/danilofreire/datasci350/pulls), [creating a discussion post](https://github.com/danilofreire/datasci350/discussions), or [contacting the instructor directly](mailto:danilo.freire@emory.edu).

## License

This repository is licensed under the [MIT License](https://github.com/danilofreire/datasci350/blob/main/LICENSE.qmd). You are free to use, modify, and distribute the materials as needed, with appropriate attribution to the original source.

-----

We look forward to an engaging and productive semester! Good luck, and happy coding! :smiley:
