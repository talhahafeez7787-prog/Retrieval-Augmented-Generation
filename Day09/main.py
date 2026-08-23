"""
main.py

Loads sentence records from sentences.json, generates embeddings using the
all-MiniLM-L6-v2 sentence-transformer model, and prints:
  1. The complete embeddings matrix shape.
  2. For every record: text, topic, embedding dimension, and first five values.
"""

import json
from pathlib import Path

from sentence_transformers import SentenceTransformer


DATA_PATH = Path(__file__).parent / "sentences.json"
MODEL_NAME = "all-MiniLM-L6-v2"


def load_records(path: Path) -> list[dict]:
    """Load sentence records from a JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        records = json.load(f)
    return records


def main() -> None:
    # 1. Load records
    records = load_records(DATA_PATH)
    texts = [record["text"] for record in records]

    topics = {record["topic"] for record in records}
    print(f"Loaded {len(records)} records across {len(topics)} topics: {sorted(topics)}\n")

    # 2. Load model and generate embeddings
    print(f"Loading model '{MODEL_NAME}'...")
    model = SentenceTransformer(MODEL_NAME)

    print("Generating embeddings...\n")
    embeddings = model.encode(texts)

    # 3. Print the complete embeddings shape
    print(f"Embeddings shape: {embeddings.shape}\n")

    # 4. Print details for every record
    for record, embedding in zip(records, embeddings):
        first_five = embedding[:5]
        formatted_values = ", ".join(f"{v:.4f}" for v in first_five)

        print(f"Text: {record['text']}")
        print(f"Topic: {record['topic']}")
        print(f"Dimension: {embedding.shape}")
        print(f"First 5 values: [{formatted_values}]")
        # print(f"Complete embedding: [{embedding}]")
        print("-" * 60)


if __name__ == "__main__":
    main()