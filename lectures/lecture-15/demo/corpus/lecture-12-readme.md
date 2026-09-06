# Lecture 12 - Local Language Models

A language model is a file. You download it, you run it from your terminal, and you can read every setting it has. This lecture puts one on your laptop, takes it apart, and then turns it into a chatbot of your own design.

[View the slides](https://danilofreire.github.io/datasci350/lectures/lecture-12/12-local-models.html)

## Before class

You must install Ollama and download the model before you arrive. Twenty-five laptops downloading 1.3 GB on the classroom wifi will not work.

1. Open <https://ollama.com/download>.
2. Download the installer for your operating system.
3. Install Ollama as you would any other application.
4. Open a new terminal window. An older window will not know where Ollama is.
5. Run `ollama --version`. A version number appears.
6. Run `ollama pull llama3.2:1b`. The download is about 1.3 GB and takes a few minutes.
7. Run `ollama run llama3.2:1b`. A `>>>` prompt appears.
8. Ask it any question, then type `/bye` to leave.

If step 5 says `command not found`, close the terminal and open a new one. That fixes it almost every time.

If your laptop cannot run the model, tell me before class. Use [Google AI Studio](https://aistudio.google.com/) in the browser in the meantime, and we will arrange a lab machine.

## What we cover

- How a model reads text: tokens rather than words, and why "ChatGPT" costs three of them
- Embeddings, where each token becomes a long list of numbers and meaning turns into geometry
- Why a trained model is a file, and what the three things inside it are
- Ollama from the terminal: `pull`, `run`, `ls`, `ps`, `show`, `stop`, `rm`
- `ollama show`, which prints the parameter count, context length, embedding length, and quantisation of the file on your disk
- Quantisation: how many bits each weight gets, and why file sizes never match parameter counts
- Choosing a model, what your RAM allows, and pulling GGUF models from Hugging Face
- System prompts, PTCF, and temperature, set live from the `>>>` prompt
- The `Modelfile`: `FROM`, `PARAMETER`, `SYSTEM`, and `MESSAGE`
- Few-shot prompting as `MESSAGE` pairs, and what examples can and cannot fix
- Structured output with `--format json`, and piping a model's answer into Python
- Hallucination and bias, on a model you can inspect

## The idea that holds it together

Part one is abstract: tokens, embeddings, thousands of dimensions. Part two runs one command, `ollama show llama3.2:1b`, and prints the whole of part one back at you:

```text
architecture llama | parameters 1.2B | context length 131072
embedding length 2048 | quantization Q8_0
```

Context length is the token limit. Embedding length is how many dimensions the king-queen space actually has. Quantisation is lecture 02's argument about abstraction, applied to the weights: a colour keeps only the detail the eye needs, and a weight keeps only the detail the answer needs.

## Numbers worth remembering

The same model at two quantisations: `llama3.2:1b` is 1.2B parameters at 8 bits each, which is 1.3 GB. The Hugging Face build of the identical model at 4 bits is 807 MB. Same architecture, same context length, same embedding length, forty per cent less file.

Seven custom personas built on one base model show as 1.3 GB each in `ollama ls`, but the models folder holds 3.4 GB in total, not 9. They share one copy of the weights.

At temperature 0, with `/clear` between the two attempts, the same prompt returned the identical sentence three times. At temperature 1 it returned three different answers, and one of them ignored the instruction to write a single line.

## Practice

Build a butler. The exercise is on the "Try it yourself!" slide and the solution is in Appendix 02.

1. Create a file called `Hobbes`, with no extension.
2. Write `FROM llama3.2:1b` on the first line.
3. Add a `PARAMETER temperature` line with a value you choose.
4. Write a `SYSTEM` block covering all four PTCF parts.
5. Make the `SYSTEM` block enforce three rules. Answer in three sentences at most. Address the user as "my dear". Admit plainly when asked to do something it cannot do.
6. Run `ollama create hobbes -f Hobbes`. The terminal prints `success`.
7. Run `ollama run hobbes`.
8. Ask it to fix a bug in your Python script.
9. Ask it for tomorrow's weather forecast for Atlanta.
10. Ask it what you asked it yesterday.
11. Write down which of your three rules it broke.
12. Add one `MESSAGE` pair showing Hobbes refusing something politely.
13. Rebuild the model and ask step 9 again.

Bring your `Hobbes` file, one transcript where the model obeyed you, and one where it did not. The second is the more interesting half, and there will be one.

Mine invented a complete weather forecast for Atlanta, cheerfully, in character, having been told in plain English that it could not check anything. Three `MESSAGE` examples improved it, but on one run in three it still made up a forecast. That result is the point of the exercise rather than a failure of it: a system prompt sets a tone reliably and a rule only approximately.

## Rendering

Run `quarto render 12-local-models.qmd` in this folder. If Quarto cannot find Python, set `QUARTO_PYTHON=~/miniconda3/bin/python3` first. The deck is self-contained HTML. No code runs at render time, and every terminal transcript on the slides was captured from a real session beforehand, so rendering needs no network and no running Ollama.

Model names, sizes, and the Hugging Face pull syntax were verified against a live Ollama 0.32.9 install in August 2026. Check them again before teaching, because the small-model shelf moves quickly.

## Before the next class

1. Complete the exercise above.
2. Keep Ollama installed. Lectures 14 and 15 both build on it.
3. Run `quarto check` on the laptop you will bring.
4. Charge the laptop and pack the charger.

Next class is Quiz 02: Literate Programming, worth 6%. It covers lectures 10 and 11: Quarto, Markdown, citations, `freeze`, and building a site. Open notes, open slides, open web, AI allowed, and you must say which AI you used.

After the quiz, lecture 14 keeps this model and changes the interface. Ollama has been running a small web server on `localhost:11434` the whole time, and Python can talk to it. Lecture 15 then closes the AI module with retrieval, which is how you make a model answer from documents instead of from memory.

## Using AI in this course

You may use AI for the assignments in this course. Cite the tool you used, check everything it gives you, and remember that the fluency of an answer tells you nothing about whether it is correct.

Using AI tools in a manner prohibited in this course syllabus constitutes Cheating under the Emory Honour Code and is thus a form of academic misconduct.
