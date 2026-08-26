"""
similarity_search.py
---------------------
A small semantic similarity search program over a JSON knowledge base of
university rules.

Pipeline:
    1. Load records (id, text, source) from knowledge_base.json
    2. Embed every record's text using the sentence-transformers model
       "all-MiniLM-L6-v2"
    3. Ask the user for a search query, embed it with the same model
    4. Compute cosine similarity between the query embedding and every
       document embedding
    5. Sort results from highest to lowest similarity
    6. Display the top 3 matches, each with its source and a rounded score
    7. Reject empty queries with a clear message

Usage:
    python3 similarity_search.py
"""

import json
import sys
import numpy as np
from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"
KB_PATH = "knowledge_base.json"
TOP_K = 3


def load_knowledge_base(path: str) -> list[dict]:
    """Load and validate the JSON knowledge base file.

    Each record is expected to have the keys: id, text, source.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            records = json.load(f)
    except FileNotFoundError:
        print(f"Error: could not find knowledge base file '{path}'.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: '{path}' is not valid JSON ({e}).")
        sys.exit(1)

    if not isinstance(records, list) or len(records) == 0:
        print("Error: knowledge base must be a non-empty JSON array of records.")
        sys.exit(1)

    for i, rec in enumerate(records):
        for key in ("id", "text", "source"):
            if key not in rec:
                print(f"Error: record at index {i} is missing required key '{key}'.")
                sys.exit(1)

    return records


def load_model(model_name: str) -> SentenceTransformer:
    """Load the sentence-transformers embedding model."""
    print(f"Loading embedding model '{model_name}' ...")
    model = SentenceTransformer(model_name)
    print("Model loaded.\n")
    return model


def embed_documents(model: SentenceTransformer, records: list[dict]) -> np.ndarray:
    """Compute embeddings for every document's text field."""
    texts = [rec["text"] for rec in records]
    embeddings = model.encode(texts, convert_to_numpy=True, normalize_embeddings=False)
    return embeddings


def cosine_similarity(query_vec: np.ndarray, doc_matrix: np.ndarray) -> np.ndarray:
    """Compute cosine similarity between one query vector and a matrix of
    document vectors. Returns an array of similarity scores, one per document.
    """
    query_norm = query_vec / (np.linalg.norm(query_vec) + 1e-10)
    doc_norms = doc_matrix / (np.linalg.norm(doc_matrix, axis=1, keepdims=True) + 1e-10)
    scores = doc_norms @ query_norm
    return scores


def search(query: str, model: SentenceTransformer, records: list[dict],
           doc_embeddings: np.ndarray, top_k: int = TOP_K) -> list[tuple[dict, float]]:
    """Embed the query, score it against every document, and return the
    top_k (record, score) pairs sorted from highest to lowest similarity.
    """
    query_vec = model.encode([query], convert_to_numpy=True)[0]
    scores = cosine_similarity(query_vec, doc_embeddings)

    ranked_indices = np.argsort(scores)[::-1]  # highest -> lowest
    top_indices = ranked_indices[:top_k]

    return [(records[i], float(scores[i])) for i in top_indices]


def display_results(results: list[tuple[dict, float]]) -> None:
    """Pretty-print the top results with source and rounded score."""
    if not results:
        print("No results found.")
        return

    print(f"\nTop {len(results)} result(s):\n" + "-" * 50)
    for rank, (rec, score) in enumerate(results, start=1):
        print(f"{rank}. Score: {round(score, 3)}")
        print(f"   Text:   {rec['text']}")
        print(f"   Source: {rec['source']}\n")


def get_valid_query() -> str:
    """Prompt the user for a query and reject empty/whitespace-only input."""
    query = input("Enter your search query: ").strip()
    if not query:
        print("Error: query cannot be empty. Please enter a valid search query.")
        return ""
    return query


def run_interactive_loop(model: SentenceTransformer, records: list[dict],
                          doc_embeddings: np.ndarray) -> None:
    """Main interactive loop: keep prompting until the user quits."""
    print("University Rules Similarity Search")
    print("Type your question below, or type 'quit' to exit.\n")

    while True:
        raw = input("Enter your search query (or 'quit' to exit): ").strip()

        if raw.lower() in ("quit", "exit"):
            print("Goodbye!")
            break

        if not raw:
            print("Error: query cannot be empty. Please enter a valid search query.\n")
            continue

        results = search(raw, model, records, doc_embeddings, top_k=TOP_K)
        display_results(results)


def main():
    records = load_knowledge_base(KB_PATH)
    model = load_model(MODEL_NAME)
    doc_embeddings = embed_documents(model, records)
    run_interactive_loop(model, records, doc_embeddings)


if __name__ == "__main__":
    main()