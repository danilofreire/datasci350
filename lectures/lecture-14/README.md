# Lecture 14 - Calling Models from Your Own Code

Last week you typed at a model. This week your code calls one, and a language model becomes a function you can map over a column.

[View the slides](https://danilofreire.github.io/datasci350/lectures/lecture-14/14-ai.html)

## What we cover

- What an API is: you send a request to an address, you get JSON back
- The server Ollama has been running on `localhost:11434` since lecture 12
- Reading a JSON response with `curl`, and what each field means
- Calling your own model from Python, with no key and no internet
- The shape of a reply: `choices`, `message.content`, `finish_reason`, and `usage`
- OpenRouter: one key, hundreds of models, some of them free
- Keeping an API key out of your repository with `.env` and `.gitignore`
- Why free text is a poor interface for a program, and how `response_format` fixes it
- Classifying a file of headlines and checking the answers against human labels
- Proving two runs are identical with `diff` and `shasum`
- What a coding agent actually is, in about twenty lines of Python
- Prompt injection, the lethal trifecta, and the ways agents fail quietly

## The idea the lecture is built on

The `openai` package is not a package for OpenAI. It is a client for a protocol many servers now speak, including the Ollama server already running on your laptop. The same twelve lines of Python talk to a 1B model on your disk or to a large hosted one, and only two constants change: the address and the key.

## Before class: get an OpenRouter key

This takes about ten minutes and the room cannot do it together at the last moment.

1. Create an account at <https://openrouter.ai/>.
2. Go to <https://openrouter.ai/keys> and create a key.
3. Set the spending limit to $0.00, so a mistake in a loop is refused rather than billed.
4. Copy the key. It starts with `sk-or-` and is shown only once.
5. Save it in a `.env` file as `OPENROUTER_API_KEY=sk-or-...`.
6. Add `.env` to your `.gitignore` before you commit anything.

Warning: a key in a public repository is found by scanners within minutes, and deleting the commit does not help. If you leak one, revoke it immediately.

Also run `pip install openai python-dotenv pandas`, and check that Ollama still starts.

To find a free model, open <https://openrouter.ai/models>, set Prompt pricing to Free, and copy an id ending in `:free`. Take the id from the catalogue rather than from memory, since providers add and retire models often.

## The demo folder

`ask_local.py` calls your local model and prints the token count. `classify.py` reads `headlines.csv`, asks for JSON, writes `results.csv`, and reports how often the model agreed with the human labels. `Classifier` is the Modelfile from lecture 12.

On my laptop `classify.py` agreed with the human labels on thirteen of fifteen headlines. Both misses were neutral ones: a new chief financial officer was called bullish, an annual report bearish. Asked to choose a direction, the model chooses one even when nothing has happened. "87% accurate" and "cannot recognise the absence of news" describe the same run, and only the second tells you where it will fail.

## Practice

The first exercise needs no key: call your local model, run it twice, turn the wifi off and run it again, then set `max_tokens=40` and read `finish_reason`.

The second needs the key: run `classify.py` locally, change the three constants, and run it against a hosted model. Write down both agreement scores and one headline where they disagreed.

For anything you report, set `temperature=0`, pin the exact model id, and save the raw responses. `diff` and `shasum` turn "it looks the same" into proof.

## Before the next class

1. Finish both exercises.
2. Keep your `.env` file and your OpenRouter key.
3. Check that Ollama still runs on the laptop you will bring.

Next class is lecture 15, the last of the AI module: retrieval-augmented generation, and a look at fine-tuning. Today the model answered from what it learned in training. Next time it answers from documents you hand it.

## Using AI in this course

You may use AI for the assignments in this course. Cite the tool you used, check everything it gives you, and remember that the fluency of an answer tells you nothing about whether it is correct.

Using AI tools in a manner prohibited in this course syllabus constitutes Cheating under the Emory Honour Code and is thus a form of academic misconduct.
