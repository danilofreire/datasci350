# Lecture 19 - Working with APIs in Practice

Last class we used web APIs from the browser and the terminal. This class we do the same work in Python. By the end you will be able to open a JSON file, follow a path to one value, send a request with `requests`, check it for errors, turn the reply into a pandas DataFrame, and save it as a CSV. We finish by reading your project's `pull_data.py`, line by line.

[View the slides](https://danilofreire.github.io/datasci350/lectures/lecture-19/19-apis-in-practice.html)

## What we cover

- Dictionaries and lists, the Python types that hold JSON
- Opening a file with `with open(...) as f:`, and `json.load`, `json.loads` and `json.dump`
- Turning a JSON path into square brackets, and reading `KeyError` and `IndexError`
- `requests.get` with `params` and `timeout`, and what the response holds
- Checking for errors with `raise_for_status()`, and the World Bank's `200` that hides one
- A `for` loop that builds a DataFrame from the records, and the `json_normalize` shortcut
- Many countries in one request, missing values, and saving to CSV
- Reading the project starter's `pull_data.py`
- API keys and pages for Track B, in the appendix
- Three exercises, each with a worked solution in the appendix

## Data snapshots

Everything the slides print came from a real request. The saved replies are in `data/`:

- `wb_gdp_bra.json` and `wb_pop_ury.json`: the files students saved with `curl` in Lecture 18
- `wb_life_expectancy_5.json`: life expectancy for Brazil, India, Japan, Nigeria and the United States, 2000 to 2024
- `wb_gdppc_2023_page1.json` to `page3`: the three pages of the pagination example in Appendix 05
- `nasa_apod.json`: a NASA API reply, from the earlier version of this lecture
- `wdi_panel.parquet`: eight indicators for 217 countries, 1990 to 2023, built by `data/build_wdi_panel.py` and used in Lecture 22

## Rendering

```bash
quarto render 19-apis-in-practice.qmd
```

No code executes at render time. Every output on the slides was captured from a real run and pasted in.

## Before the next class

1. Email me your group's names by Thursday 5 November, or I assign you a group at random.
2. Clone the [starter repository](https://github.com/danilofreire/datasci350-project-starter) and run `python scripts/pull_data.py` once.
3. Finish Exercise 03 if you did not have time in class.
4. Revise Lectures 12, 14, 15, 16 and 17 for Quiz 03 on Thursday 5 November.
5. Optional: the web-scraping tutorial (`tutorials/05-web-scraping-tutorial.qmd`), for when the data sits on a page and there is no API.

## Using AI in this course

You may use AI for the assignments in this course. Cite the tool you used, check everything it gives you, and remember that the fluency of an answer tells you nothing about whether it is correct.

Using AI tools in a manner prohibited in this course syllabus constitutes Cheating under the Emory Honour Code and is thus a form of academic misconduct.
