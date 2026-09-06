"""A minimal RAG pipeline over the course's own notes.

Requires a running Ollama and two models:
    ollama pull embeddinggemma
    ollama pull llama3.2:1b
And two Python packages:
    pip install ollama numpy

Usage:
    python rag.py "What does Quiz 02 cover?"
"""

import sys
from pathlib import Path

import numpy as np
import ollama

EMBED_MODEL = "embeddinggemma"
CHAT_MODEL = "llama3.2:1b"
TOP_K = 3


def load_chunks(folder):
    """Split every markdown file into paragraph chunks."""
    chunks = []
    for path in sorted(Path(folder).glob("*.md")):
        for block in path.read_text(encoding="utf-8").split("\n\n"):
            block = block.strip()
            if len(block) > 80:
                chunks.append((path.name, block))
    return chunks


def embed(texts):
    """Turn a list of texts into one vector per text."""
    response = ollama.embed(model=EMBED_MODEL, input=texts)
    return np.array(response["embeddings"])


def main():
    question = sys.argv[1] if len(sys.argv) > 1 else "What does this course cover?"
    chunks = load_chunks(Path(__file__).parent / "corpus")
    files = {name for name, _ in chunks}
    print(f"Corpus: {len(chunks)} chunks from {len(files)} files")

    chunk_vectors = embed([text for _, text in chunks])
    question_vector = embed([question])[0]

    # Cosine similarity is a dot product once every vector has length 1
    chunk_vectors /= np.linalg.norm(chunk_vectors, axis=1, keepdims=True)
    question_vector /= np.linalg.norm(question_vector)
    scores = chunk_vectors @ question_vector

    top = np.argsort(scores)[::-1][:TOP_K]
    print("\nRetrieved chunks:")
    for i in top:
        name, text = chunks[i]
        print(f"  [{scores[i]:.3f}] {name}: {text[:70]}...")

    context = "\n\n".join(chunks[i][1] for i in top)
    prompt = (
        "Answer the question using ONLY the context below. "
        "If the answer is not in the context, say you do not know.\n\n"
        f"Context:\n{context}\n\nQuestion: {question}"
    )
    reply = ollama.chat(model=CHAT_MODEL, messages=[{"role": "user", "content": prompt}])
    print(f"\nAnswer:\n{reply.message.content}")


if __name__ == "__main__":
    main()
