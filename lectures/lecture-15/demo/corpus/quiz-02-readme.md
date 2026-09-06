# Lecture 13 - Quiz 02: Literate Programming

Quiz day. There are no slides for this session, and no new material. You spend the class working on the quiz.

## The repository

<https://github.com/danilofreire/datasci350-quiz02>

The link opens at the start of class. Fork it to your own account first, then clone your fork to your machine. You cannot push to my copy, so cloning it directly is the quickest way to lose time.

## What the quiz is

- Worth 6% of the final grade
- You have the whole class period
- It covers lectures 10 and 11: Quarto documents, Markdown, chunk options, cross-references, `freeze`, websites, and publishing
- The repository holds a small film box-office dataset. You build a four-page Quarto website from it and publish the site on GitHub Pages

You write no difficult Python. The quiz grades your Quarto and your Git work, and the plotting patterns from the lecture 11 examples are enough throughout. Where a task needs an idiom we have not covered, the code is given to you.

## How to submit

Post **two links** on Canvas, in the "Assignments" tab, under Quiz 02:

1. The link to your published website
2. The link to your fork

One link is half a submission. Check that the fork URL has your own username in it before you post it.

## Rules

- Open-book and open-notes. You may use your slides, your notes, and the web
- It is an individual assessment. Do not discuss the questions with your colleagues during class
- You must be able to explain every command and every line you submit. I may ask any of you to walk through part of your work, during the quiz or straight after it
- Work from the command line and your editor throughout. Files created or uploaded through the GitHub website lose marks, because the grader reads your commit history
- Record every command you run in `commands.txt`, in the root of the repository. Where a task asks for a short explanation, write it there too
- State which AI tools you used on the website's home page. The syllabus AI policy applies

Using AI tools in a manner prohibited in this course syllabus constitutes Cheating under the Emory Honour Code and is thus a form of academic misconduct.

## Before you arrive

1. Run `quarto check`. Every line should pass.
2. Render any Quarto document on the laptop you are bringing.
3. Publish a small test site with `quarto publish gh-pages` from a scratch repository.
4. Push something to GitHub from that same laptop.
5. Charge your laptop and pack the charger.

Step 3 is the one people skip, and it is the one that fails on the day. Ten minutes now saves twenty in the quiz.

If a push fails with an authentication error, do not start creating tokens. Run `gh auth login`, choose GitHub.com, then HTTPS, then log in with the browser. After that `git push` and `quarto publish` behave normally.

## What costs marks

None of these is about knowing Quarto:

- Cloning my repository instead of forking it first, so the push is rejected
- Building the site through the GitHub website instead of from your machine
- Rendering the site but never committing the `_freeze/` folder
- Publishing the site and never opening the published link to check that it works
- Leaving `commands.txt` empty, or forgetting to create it
- Submitting one link instead of two

Running `git status` and `pwd` often prevents most of them. Opening your own published site prevents the rest.

## If you finish early

There are two bonus tasks at the end of the quiz README. Attempt them only once the main tasks are done, and document every step in `commands.txt` as usual.
