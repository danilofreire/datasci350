# Lecture 18 - Web APIs and JSON

Last class you rented a machine and typed into it over SSH. This class your own laptop asks other people's servers for data. By the end you will know what happens between a URL and a Python dictionary: how the request is built, what the status code tells you, why the response arrives as JSON, and how three lines of `requests` cover the whole journey. You did this once already in Lecture 14, when you sent a prompt to a language model. Today we open the box.

[View the slides](https://danilofreire.github.io/datasci350/lectures/lecture-18/18-web-apis.html)

## What we cover

- What an API is: a contract between two programs, and the client-server model you met on EC2
- Anatomy of a URL: scheme, host, path, and the query string after the `?`
- `GET` and `POST`, and why almost everything you do this semester is a `GET`
- Status codes, including the `200` that hides an error in the body
- JSON, and how it maps onto Python dictionaries and lists
- Digging into nested responses, and the World Bank's two-element list
- The `requests` library: `params`, `timeout`, `raise_for_status()`, and `.json()`
- A worked example: Brazilian GDP per capita from 2014 to 2025
- How to read a reference page: find the example request first, then the parameter table
- Three exercises, each with a worked solution in the appendix. Headers get a preview in Appendix 05

## Data snapshots

Three JSON files live in `data/`: `openmeteo_atlanta.json`, `wb_gdp_bra.json`, and `wb_pop_ury.json`. All three were pulled on 21 August 2026. The deck reads them from disk and renders with no network connection, so the numbers on the slides stay put.

## Rendering

```bash
quarto render 18-web-apis.qmd
```

No code executes at render time. Every output on the slides was captured from a real request and pasted in.

## Before the next class

1. Install the packages you will need: `pip install requests pandas pyarrow`.
2. Open the AWS billing console and confirm your total reads zero.
3. Read the final project instructions.
4. Form a group of three to four and email me the names by Thursday 5 November.
5. Try the Uruguay exercise in Appendix 03

API claims last verified: 21 August 2026 (the World Bank lists 29,544 indicators).

## Using AI in this course

You may use AI for the assignments in this course. Cite the tool you used, check everything it gives you, and remember that the fluency of an answer tells you nothing about whether it is correct.

Using AI tools in a manner prohibited in this course syllabus constitutes Cheating under the Emory Honour Code and is thus a form of academic misconduct.
