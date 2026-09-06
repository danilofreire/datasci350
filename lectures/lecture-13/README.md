# Lecture 13 - Quiz 02: Literate Programming

Quiz day. There are no slides and no new material. You spend the class working on the quiz.

## The repository

<https://github.com/danilofreire/datasci350-quiz02>

The link opens at the start of class. Fork it first, then clone your fork. You cannot push to my copy.

## What the quiz is

- Worth 6% of the final grade, and you have the whole class period
- It covers lectures 10 and 11: Quarto documents, Markdown, chunk options, cross-references, `freeze`, websites, and publishing
- You build a four-page Quarto website from a film box-office dataset and publish it on GitHub Pages

You write no difficult Python. The plotting patterns from lecture 11 are enough, and where a task needs an idiom we have not covered, the code is given to you.

## Rules

- Open-book and open-notes. You may use your slides, your notes, and the web
- Individual assessment. Do not discuss the questions with your colleagues in class
- You must be able to explain every command and every line you submit
- Work from the command line and your editor. Files created through the GitHub website lose marks, because the grader reads your commit history
- Record every command in `commands.txt` in the root of the repository
- State which AI tools you used on the website's home page

Using AI tools in a manner prohibited in this course syllabus constitutes Cheating under the Emory Honour Code and is thus a form of academic misconduct.

## How to submit

Post **two links** on Canvas, under Quiz 02: your published website, and your fork. One link is half a submission.

## Before you arrive

1. Run `quarto check`. Every line should pass.
2. Render any Quarto document on the laptop you are bringing.
3. Publish a small test site with `quarto publish gh-pages` from a scratch repository.
4. Charge your laptop and pack the charger.

Step 3 is the one people skip, and the one that fails on the day. If a push fails with an authentication error, run `gh auth login` rather than creating tokens.

## What costs marks

Cloning instead of forking, building the site through the GitHub website, rendering but never committing `_freeze/`, never opening your published link to check it works, leaving `commands.txt` empty, or submitting one link instead of two.

If you finish early, there are two bonus tasks at the end of the quiz README.
