"""Ask your own model a question, from Python instead of the terminal.

Needs Ollama running and llama3.2:1b pulled, both from lecture 12.

    pip install openai
    python3 ask_local.py
"""

from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",  # the library insists on one; Ollama ignores it
)

response = client.chat.completions.create(
    model="llama3.2:1b",
    messages=[{"role": "user", "content": "Why is the sky blue?"}],
    temperature=0,
)

print(response.choices[0].message.content)
print()
print(response.usage)
