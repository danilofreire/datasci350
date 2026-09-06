# Lecture 15 - Retrieval-Augmented Generation and Fine-Tuning

The last lecture of the AI module. Lecture 12 put a model on your laptop, lecture 14 called one from your own code, and this one answers the question both left open: how do you make a model answer questions about documents it has never read?

[View the slides](https://danilofreire.github.io/datasci350/lectures/lecture-15/15-rag-finetuning.html)

## What we cover

- Embeddings for whole passages, and cosine similarity in one line of numpy
- Getting embeddings from Ollama with `embeddinggemma`
- The five stages: chunk, embed, store, retrieve, generate, and where each one fails
- Why retrieval beats pasting everything in: the cost arithmetic, and "lost in the middle"
- A working pipeline in about 50 lines of plain Python (`demo/rag.py`), read line by line
- Measuring retrieval with gold questions and a hit rate
- Hybrid search, BM25, and rerankers, for the questions embeddings get wrong
- Prompt injection through a poisoned corpus, and three partial defences
- Fine-tuning: context versus weights, LoRA, and Unsloth
- Distillation, and the dispute it started
- The ladder: prompt, then RAG, then fine-tune, climbed only when the rung below fails

## Before class

Warning: the two model downloads total about 2 GB. Do not attempt them on classroom wifi.

1. Install or update Ollama from [ollama.com](https://ollama.com/).
2. Run `ollama pull embeddinggemma`.
3. Run `ollama pull llama3.2:1b`.
4. Run `pip install ollama numpy`.

If `ollama pull embeddinggemma` fails, your Ollama is too old. Update the application, or fall back to `nomic-embed-text` (274 MB). If you cannot run local models, use the OpenRouter variant in Appendix 03 with your key from lecture 14.

## The demo folder

`demo/rag.py` is the whole pipeline in one file, and `demo/corpus/` holds eight of this course's own READMEs, which chunk into 132 passages. Run it with a question:

```bash
python rag.py "What does Quiz 02 cover?"
```

It prints the corpus size, the three retrieved chunks with their scores, and the answer. Printing the chunks is the point: when an answer is wrong, they tell you whether retrieval or generation failed.

## What the evaluation found

Seven gold questions, five retrieved the right file. Both misses were questions the corpus cannot answer, since no file gives a quiz date or the final project's weight.

The instructive one is "When is Quiz 02?". It scored 0.58, higher than any question that succeeded, and returned a paragraph with no date in it. A confidence threshold would have passed it straight to the model. A high score means the topic matched, never that the answer is present.

Retrieval also repeats and generation does not. Run the script four times and the scores are identical, while the written answer can still change.

## Practice

Run the pipeline, check each answer against the file it cites, then ask "What is the capital of Nepal?" and watch both stages. Retrieval always returns three chunks, because the top three of whatever exists is still three, and only the prompt's escape hatch can decline. Finally set `TOP_K` to 1 and find which questions break first.

Notes are in Appendix 01 and troubleshooting in Appendix 04.

## Before the next class

1. Finish the exercise.
2. Keep Ollama and both models on the laptop you will bring.

Next class starts the cloud module. Every computer in this course has been yours so far, and next we borrow someone else's. Quiz 03 covers the AI module and the cloud module.

## Using AI in this course

You may use AI for the assignments in this course. Cite the tool you used, check everything it gives you, and remember that the fluency of an answer tells you nothing about whether it is correct.

Using AI tools in a manner prohibited in this course syllabus constitutes Cheating under the Emory Honour Code and is thus a form of academic misconduct.
