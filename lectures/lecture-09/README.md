# Lecture 09 - Quiz 01: Git and GitHub

Quiz day. There are no slides and no new material. You spend the class working on the quiz.

## The repository

<https://github.com/danilofreire/datasci350-quiz01>

Fork it to your own account first, then clone your fork. You cannot push to my copy, so cloning it directly is the quickest way to lose time.

## What the quiz is

- Worth 6% of the final grade, and you have the whole class period
- It covers lectures 02 to 07: the command line, file management, text tools, Git, and GitHub
- You take over a small climate-station project, reorganise it from the command line, and record everything you do

## Rules

- Open-book and open-notes. You may use your slides, your notes, and the web
- Individual assessment. Do not discuss the questions with your colleagues in class
- You must be able to explain every command you submit. I may ask you to walk through part of your work
- Work from the command line throughout. Files created through the GitHub website lose marks, because the grader reads your commit history
- Record every command in `commands.txt` (or `commands.ipynb`) in the root of the repository

## How to submit

Post the link to **your fork** on Canvas, under Quiz 01. Check the URL has your own username in it.

## Before you arrive

1. Run `git config --list`. It should show your name and email.
2. Push something small to GitHub from the laptop you are bringing. If that works, the quiz will work.
3. Charge your laptop and pack the charger.

If a push fails with an authentication error, do not start creating tokens. Run `gh auth login`, choose GitHub.com, then HTTPS, then log in with the browser.

## What costs marks

Cloning instead of forking, never pushing, leaving `commands.txt` empty, submitting a link to my repository, or working in the wrong directory. Running `git status` and `pwd` often prevents nearly all of them.

If you finish early, there are two bonus tasks at the end of the quiz README. Document them in `commands.txt` as usual.
