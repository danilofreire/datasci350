# Lecture 20 - Quiz 03: AI-Assisted Programming and Cloud Computing

Quiz day. There are no slides and no new material. You spend the class working on the quiz.

## The repository

<https://github.com/danilofreire/datasci350-quiz03>

The link opens at the start of class. Fork it first, then clone your fork. You cannot push to my copy.

## What the quiz is

- Worth 6% of the final grade, and you have the whole class period
- It covers lectures 12, 14, 15, 16 and 17: local models with Ollama, calling models from Python, API keys, RAG, and AWS EC2
- You build a chatbot with a `Modelfile`, call it from a Python script, then run an analysis on an EC2 instance and bring the results back

Every command in the quiz appears in the lecture slides. Revise the exercises from those lectures and you will be well prepared.

## Rules

- Open-book and open-notes. You may use your slides, your notes, and the web
- Individual assessment. Do not discuss the questions with your colleagues in class
- You must be able to explain every command and every line you submit
- Work from the command line and your editor. Files created through the GitHub website lose marks, because the grader reads your commit history
- Record every command in `commands.txt` in the root of the repository
- Screenshots are not accepted. Model responses and terminal output go in as copy-pasted text

Using AI tools in a manner prohibited in this course syllabus constitutes Cheating under the Emory Honour Code and is thus a form of academic misconduct.

## How to submit

Post the link to your fork on Canvas, under Quiz 03.

## Before you arrive

1. Run `ollama ls` and check `llama3.2:1b` or `gemma3:1b` is installed. Pull one now, on campus wifi, before the quiz
2. Confirm you can log in to the AWS console and that your zero-spend budget shows Healthy
3. Find your `.pem` key file, or be ready to create a new key pair on the day
4. Charge your laptop and pack the charger

Step 1 is the one people skip. A 1 GB download at the start of class eats your quiz time.

## What costs marks

Cloning instead of forking, uploading files through the GitHub website, pasting screenshots instead of text, committing your `.pem` key or a real API key, leaving your EC2 instance running after the quiz, or leaving `commands.txt` empty.

If you finish early, there are two bonus tasks at the end of the quiz README.
