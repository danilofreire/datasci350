"""A minimal RAG pipeline over the course's own notes.

Requires a running Ollama and two models:
    ollama pull embeddinggemma
    ollama pull llama3.2:1b
And one Python package:
    pip install ollama

Change QUESTION below, then run from inside this folder: python rag.py
"""

import math
from pathlib import Path

import ollama

EMBED_MODEL = "embeddinggemma"
CHAT_MODEL = "llama3.2:1b"
TOP_K = 3
QUESTION = "What does Quiz 02 cover?"
CORPUS = "corpus"   # the folder of notes, next to this script


def embed(texts):
    """Turn a list of texts into one vector per text."""
    response = ollama.embed(model=EMBED_MODEL, input=texts)
    return response["embeddings"]


def cosine(a, b):
    """Cosine similarity between two vectors of the same length."""
    dot = 0.0
    length_a = 0.0
    length_b = 0.0
    for i in range(len(a)):
        dot = dot + a[i] * b[i]
        length_a = length_a + a[i] * a[i]
        length_b = length_b + b[i] * b[i]
    return dot / (math.sqrt(length_a) * math.sqrt(length_b))


# Split every markdown file into paragraph chunks
chunks = []
for path in sorted(Path(CORPUS).glob("*.md")):
    text = path.read_text(encoding="utf-8")
    for paragraph in text.split("\n\n"):
        clean = paragraph.strip()
        if len(clean) > 80:
            chunks.append((path.name, clean))

files = set()
for name, text in chunks:
    files.add(name)
print(f"Corpus: {len(chunks)} chunks from {len(files)} files")

chunk_texts = []
for name, text in chunks:
    chunk_texts.append(text)

chunk_vectors = embed(chunk_texts)
question_vector = embed([QUESTION])[0]

scores = []
for vector in chunk_vectors:
    scores.append(cosine(vector, question_vector))

ranked = []
for i in range(len(chunks)):
    ranked.append((scores[i], chunks[i]))
ranked.sort(reverse=True)
top = ranked[:TOP_K]

print("\nRetrieved chunks:")
for score, chunk in top:
    name, text = chunk
    print(f"  [{score:.3f}] {name}: {text[:70]}...")

passages = []
for score, chunk in top:
    passages.append(chunk[1])
context = "\n\n".join(passages)

prompt = (
    "Answer the question using ONLY the context below. "
    "If the answer is not in the context, say you do not know.\n\n"
    f"Context:\n{context}\n\nQuestion: {QUESTION}"
)
reply = ollama.chat(model=CHAT_MODEL, messages=[{"role": "user", "content": prompt}])
print(f"\nAnswer:\n{reply.message.content}")
