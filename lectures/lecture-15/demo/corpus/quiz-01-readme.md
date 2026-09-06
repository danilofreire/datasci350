# Lecture 09 - Quiz 01: Git and GitHub

Quiz day. There are no slides for this session, and no new material. You spend the class working on the quiz.

## The repository

<https://github.com/danilofreire/datasci350-quiz01>

Fork it to your own account first, then clone your fork to your machine. You cannot push to my copy, so cloning it directly is the quickest way to lose time.

## What the quiz is

- Worth 6% of the final grade
- You have the whole class period
- It covers lectures 02 to 07: the command line, file management, text tools, Git, and GitHub
- The repository holds a small climate-station project. You take over as its maintainer, reorganise it from the command line, and record everything you do

## How to submit

Post the link to **your fork** on Canvas, in the "Assignments" tab, under Quiz 01.

A link to my repository is not a submission. Check the URL has your own username in it before you post it.

## Rules

- Open-book and open-notes. You may use your slides, your notes, and the web
- It is an individual assessment. Do not discuss the questions with your colleagues during class
- You must be able to explain every command you submit. I may ask any of you to walk through part of your work, during the quiz or straight after it
- Work from the command line throughout. Files created or uploaded through the GitHub website lose marks, because the grader reads your commit history
- Record every command you run in `commands.txt` (or a Jupyter notebook named `commands.ipynb`) in the root of the repository

## Before you arrive

1. Run `git config --list`. It should show your name and your email address.
2. Push something small to GitHub from the laptop you are bringing. Any repository will do.
3. If that push works, the quiz will work. If it does not, fix it now rather than on the day.
4. Charge your laptop and pack the charger.

If a push fails with an authentication error, do not start creating tokens. Run `gh auth login`, choose GitHub.com, then HTTPS, then log in with the browser. After that `git push` behaves normally. The review session in Lecture 08 covers this.

## What costs marks

None of these is about knowing Git:

- Cloning my repository instead of forking it first, so the push is rejected
- Committing everything and never pushing, so the repository looks empty
- Leaving `commands.txt` empty, or forgetting to create it
- Submitting a link to my repository rather than to your own fork
- Working for an hour in the wrong directory

Running `git status` and `pwd` often prevents nearly all of them.

## If you finish early

There are two bonus tasks at the end of the quiz README. Attempt them only once the main tasks are done, and document every step in `commands.txt` as usual.
