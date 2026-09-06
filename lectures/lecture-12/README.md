# Lecture 12 - Local Language Models

A language model is a file. Today you download one onto your laptop, run it from the terminal, and turn it into your own chatbot.

[View the slides](https://danilofreire.github.io/datasci350/lectures/lecture-12/12-local-models.html)

## What we cover

- How a model reads text: tokens rather than words, and embeddings, where meaning turns into geometry
- Why a trained model is a pile of learned numbers, and why that means it fits on a disk
- Ollama: install it, pull a model, chat with it, and inspect it
- Quantisation, and why a "1 billion parameter" model is never 1 GB
- How much RAM you need, and Hugging Face for models the Ollama library does not carry
- System prompts, PTCF, and temperature
- The `Modelfile`, which turns settings and a personality into a file you can commit
- Few-shot examples with `MESSAGE`, and structured output with `--format json`
- Hallucination and bias, demonstrated on a model you can open

## The commands worth memorising

| Command | What it does |
| ------- | ------------ |
| `ollama pull <model>` | Download a model |
| `ollama run <model>` | Start a conversation |
| `ollama ls` | List what you have downloaded |
| `ollama show <model>` | Print a model's details |
| `ollama rm <model>` | Delete it from disk |

Inside the chat, `/set parameter temperature 0` changes a setting, `/clear` forgets the conversation, and `/bye` leaves.

## What a system prompt can and cannot do

Jeeves, the sarcastic butler we build in class, holds his tone perfectly. Told to admit when he cannot do something, he invented a weather forecast for Atlanta instead. A system prompt sets a tone reliably and a rule only approximately.

`/clear` matters more than it looks: inside one session the model sees its own previous answers, so asking the same question twice is not the same experiment twice.

## Practice

Install Ollama before class from <https://ollama.com/download>, then run `ollama pull llama3.2:1b`. The download is 1.3 GB and slow on university wifi.

The second exercise asks you to build Hobbes, a relentlessly cheerful butler: write a `Modelfile` with a `SYSTEM` block using all four parts of PTCF, give him three rules, run `ollama create hobbes -f Hobbes`, then find which rule he breaks. Bring one transcript where he obeyed and one where he did not.

## Before the next class

1. Install Ollama and pull `llama3.2:1b`.
2. Complete both exercises.
3. Check that `quarto render` and `git push` both work on the laptop you will bring.

If `ollama` is not found, open a new terminal. If answers arrive one word at a time, the model does not fit in RAM: close your browser, or try `gemma3:1b`.

Next class is Quiz 02: Literate Programming, worth 6%, covering lectures 10 and 11. After the quiz, lecture 14 keeps the model and changes the interface: Ollama has been running a web server on `localhost:11434` all along, and Python can talk to it. Keep Ollama installed.
