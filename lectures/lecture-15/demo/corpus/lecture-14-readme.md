# Lecture 14 - Calling Models from Your Own Code

Last week you typed at a model. This week your code calls one, and a language model becomes a function you can map over a column.

[View the slides](https://danilofreire.github.io/datasci350/lectures/lecture-14/14-ai.html)

## What we cover

- What an API is: you send a request to an address, you get JSON back
- The server you have been running since lecture 12, on `localhost:11434`
- Reading a JSON response with `curl`, and what each field of it means
- Calling your own model from Python, with no key and no internet
- The shape of a reply: `choices`, `message.content`, `finish_reason`, and `usage`
- What tokens cost, and why a long conversation costs more per reply than a short one
- OpenRouter: one key, hundreds of models, some of them free
- Keeping an API key out of your repository with `.env` and `.gitignore`
- Swapping from your laptop to a hosted model by changing an address
- Why free text is a poor interface for a program, and how `response_format` fixes it
- Classifying a whole file of headlines and checking the answers against human labels
- Proving two runs are identical with `diff` and `shasum`
- What a coding agent actually is, in about twenty lines of Python
- Prompt injection, the lethal trifecta, and the ways agents fail quietly

## Looking at the API with curl

Ask your own machine which models it is holding:

```bash
curl http://localhost:11434/api/tags
```

The reply arrives as one long line, because the program reading it does not need the newlines. Pipe it through a formatter to read it yourself:

```bash
curl -s http://localhost:11434/api/tags | python3 -m json.tool
```

Three parts of that second command are worth naming:

- `-s` hides the download progress meter, so only the response is printed.
- `|` is the pipe from lecture 04. It feeds what `curl` printed into the next command.
- `python3 -m` runs a module that ships with Python instead of a file of your own. `json.tool` is the module that indents JSON.

If `curl` prints `Connection refused`, the server is not running. Open the Ollama application, or run `ollama serve` in another terminal.

## The idea the lecture is built on

The `openai` package is not a package for OpenAI. It is a client for a protocol that many servers now speak, including the Ollama server already running on your laptop.

So the same twelve lines of Python talk to a 1B model on your own disk or to a large hosted one, and the only difference is two constants:

```python
# On your laptop
BASE_URL = "http://localhost:11434/v1"
API_KEY = "ollama"
MODEL = "llama3.2:1b"

# Somewhere else
BASE_URL = "https://openrouter.ai/api/v1"
API_KEY = os.environ["OPENROUTER_API_KEY"]
MODEL = "openai/gpt-oss-20b:free"
```

Develop against the local one, where there is no key, no quota and no bill. Move to the hosted one only when you can say what you are buying.

## Before class: get an OpenRouter key

This takes about ten minutes and the room cannot do it together at the last moment.

1. Create an account at <https://openrouter.ai/>. An email address is enough.
2. Go to <https://openrouter.ai/keys> and create a new key.
3. Give the key a name.
4. Set the spending limit to $0.00. A mistake in a loop is then refused rather than billed.
5. Copy the key. It starts with `sk-or-` and it is shown only once.
6. Save it in a file called `.env` as `OPENROUTER_API_KEY=sk-or-...`.
7. Add `.env` to your `.gitignore` before you commit anything.

Warning: a key in a public repository is found by automated scanners within minutes. Deleting the commit does not help, because git keeps history. If you leak a key, revoke it immediately and make a new one.

Also run `pip install openai python-dotenv pandas`, and check that Ollama still starts.

## Choosing a model on OpenRouter

Finding a free model takes three clicks:

1. Open <https://openrouter.ai/models>.
2. Set Prompt pricing to Free.
3. Open the Text tab and copy an id ending in `:free`.

An id looks like `company/model-name`, and that string is all you change to switch models. Three that worked in August 2026: `openai/gpt-oss-20b:free`, `google/gemma-4-31b-it:free`, and `nvidia/nemotron-nano-9b-v2:free`. Providers add and retire models often, so take the id from the catalogue rather than from memory.

The model's own page is where the choice is made. It shows the context length in tokens, the price per million tokens listed separately for input and output, and which company actually serves it.

Free access is paid for somehow. Read the data policy before you send anything you would not publish, and never send student data, personal data, or anything under an NDA.

The free tier allows 20 requests per minute and 50 per day, or 1,000 per day once you have added $10 of credit. That is why the exercise uses fifteen headlines and not five hundred.

## The demo folder

- `ask_local.py` calls your local model and prints the answer and the token count
- `classify.py` reads `headlines.csv`, asks the model for JSON, writes `results.csv`, and reports how often the model agreed with the human labels
- `headlines.csv` holds fifteen headlines with a `human_label` column
- `Classifier` is the Modelfile from lecture 12, if you would rather bake the system prompt into the model than send it every call

Both scripts run against Ollama with no key. On my laptop `classify.py` finished fifteen headlines in 5.8 seconds and agreed with the human labels on thirteen of them.

Where the two misses fall matters more than the score:

| Human label | Headlines | Model agreed |
| ----------- | --------- | ------------ |
| bullish | 5 | 5 |
| bearish | 6 | 6 |
| neutral | 4 | 2 |

Every bullish and every bearish headline was right, and half the neutral ones were wrong. A new chief financial officer was called bullish, and an annual report scheduled for Thursday was called bearish. Asked to choose a direction, the model chooses one, even when nothing has happened yet. "87% accurate" and "cannot recognise the absence of news" describe the same run, and only the second one tells you where it will fail.

## Reproducibility

An API call is the hardest place in this course to be reproducible. The model is on someone else's computer, it is versioned by someone else, and it can change without telling you.

Three habits:

- Set `temperature=0` for anything you will report
- Pin the exact model id, never a moving alias
- Save the raw responses, the model id, and the date beside your results

Run `classify.py` twice against your local model, then compare the two files:

```bash
diff run1.csv run2.csv
shasum run1.csv run2.csv
```

`diff` prints only the lines that differ, so it says nothing when the files match. `shasum` reduces each file to forty hexadecimal characters, so identical fingerprints are something you can see. Mine matched. That is what temperature 0 and a pinned model bought.

`shasum` is the same kind of fingerprint as the `digest` field the Ollama API reports for a model, which is how you state exactly which weights produced a result.

## Practice

Both exercises are on the slides, with solutions in the appendix.

The first needs no key: install `openai`, call your local model, run it twice, turn the wifi off and run it again, then add `max_tokens=40` and look at what `finish_reason` says.

The second needs the key: run `classify.py` locally, then change the three constants at the top and run it against a hosted model. Write down the agreement score for each and one headline where the two disagreed.

## Before the next class

1. Finish both exercises.
2. Check that Ollama still runs on the laptop you will bring.
3. Keep your `.env` file and your OpenRouter key.

Next class is lecture 15, the last of the AI module: retrieval-augmented generation, and a look at fine-tuning. Today the model answered from what it learned during training. Next time it answers from documents you hand it, which is how you point a model at material it has never seen. The embeddings from lecture 12 stop being a diagram and start doing work.

Quiz 03 on 5 November covers the AI and cloud modules.

## Using AI in this course

You may use AI for the assignments in this course. Cite the tool you used, check everything it gives you, and remember that the fluency of an answer tells you nothing about whether it is correct.

Using AI tools in a manner prohibited in this course syllabus constitutes Cheating under the Emory Honour Code and is thus a form of academic misconduct.
