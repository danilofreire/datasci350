"""Classify a file of headlines with a model, then check the answers.

Runs against your local Ollama by default. To use OpenRouter instead,
change BASE_URL, API_KEY and MODEL. Nothing else changes.

    pip install openai pandas
    python3 classify.py
"""

import json

import pandas as pd
from openai import OpenAI

BASE_URL = "http://localhost:11434/v1"
API_KEY = "ollama"
MODEL = "llama3.2:1b"

SYSTEM = (
    "You classify news headlines. Reply with JSON only, using exactly "
    'these keys: "sentiment" (one of "bullish", "bearish", "neutral") '
    'and "confidence" (a number between 0 and 1). Add no other text.'
)

client = OpenAI(base_url=BASE_URL, api_key=API_KEY)


def classify(headline):
    """Send one headline to the model and return the parsed JSON."""
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": headline},
        ],
        temperature=0,
        response_format={"type": "json_object"},
    )
    return json.loads(response.choices[0].message.content)


headlines = pd.read_csv("headlines.csv")
headlines["model_label"] = [classify(h)["sentiment"] for h in headlines["headline"]]
headlines.to_csv("results.csv", index=False)

agreed = headlines["model_label"] == headlines["human_label"]
print(headlines[["headline", "human_label", "model_label"]].to_string(index=False))
print()
print(f"Model agreed with the human on {agreed.sum()} of {len(agreed)} headlines")
