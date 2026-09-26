# RAG demo: ask the course about itself

A minimal retrieval-augmented generation pipeline in one file, `rag.py`. It answers questions about the markdown files in `corpus/`, which are copies of this course's own READMEs. No vector database, no framework: paragraph chunking, Ollama embeddings, cosine similarity written out as a loop, and a grounded prompt to a small local chat model.

## Setup

Warning: the two model downloads total about 2 GB. Use a good connection.

1. Install Ollama from [ollama.com](https://ollama.com/).
2. Run `ollama pull embeddinggemma`.
3. Run `ollama pull llama3.2:1b`.
4. Run `pip install ollama`.

## Run it

1. Open `rag.py` and set the `QUESTION` constant to the question you want to ask.
2. Run `python rag.py`.
3. The script prints the corpus size, the three retrieved chunks with their similarity scores, and the model's answer.

Then experiment:

- Set `QUESTION` to something the corpus can answer, and check the answer against the named file.
- Set `QUESTION` to something the corpus cannot answer ("What is the capital of Nepal?") and watch how retrieval and generation each behave.
- Change `TOP_K` in `rag.py` from 3 to 1 and see which questions degrade.
- Point `CORPUS` at a folder of your own notes.

If `ollama pull embeddinggemma` fails, update Ollama, or switch `EMBED_MODEL` to `nomic-embed-text` and pull that instead.

The lecture slides (`../15-rag-finetuning.qmd`) walk through the script in detail, and the appendix has an OpenRouter variant for laptops that cannot run local models.
