"""
Course Knowledge Search Engine
-------------------------------
A small semantic search tool built on top of a persistent ChromaDB
collection. Course notes are stored in knowledge_base.json, embedded
into a local ChromaDB collection, and searched with natural-language
queries typed by the user.

Run with:  python main.py
Type a query and press Enter to search.
Type 'exit' to quit.
"""

import json
import os
import sys

import chromadb

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
KNOWLEDGE_BASE_FILE = "knowledge_base.json"
CHROMA_DB_DIR = "chroma_db"
COLLECTION_NAME = "course_knowledge"
TOP_K = 3


def load_knowledge_base(path: str) -> list:
    """Load the knowledge base records from a JSON file."""
    if not os.path.exists(path):
        print(f"Error: could not find knowledge base file '{path}'.")
        sys.exit(1)

    with open(path, "r", encoding="utf-8") as f:
        records = json.load(f)

    # Basic validation: every record needs a unique id, source, category, text.
    seen_ids = set()
    for record in records:
        for field in ("id", "text", "source", "category"):
            if field not in record or not str(record[field]).strip():
                raise ValueError(f"Record missing required field '{field}': {record}")
        if record["id"] in seen_ids:
            raise ValueError(f"Duplicate id found in knowledge base: {record['id']}")
        seen_ids.add(record["id"])

    return records


def get_collection():
    """Create (or load) a persistent ChromaDB collection."""
    client = chromadb.PersistentClient(path=CHROMA_DB_DIR)
    collection = client.get_or_create_collection(name=COLLECTION_NAME)
    return collection


def populate_collection(collection, records: list) -> None:
    """Insert knowledge base records into the collection if it's empty.

    Uses ChromaDB's default embedding function under the hood (set when
    the collection was created), so we only need to hand over the raw
    document text plus IDs and metadata.
    """
    if collection.count() > 0:
        print(f"Collection already has {collection.count()} documents. Skipping insert.")
        return

    ids = [r["id"] for r in records]
    documents = [r["text"] for r in records]
    metadatas = [{"source": r["source"], "category": r["category"]} for r in records]

    collection.add(ids=ids, documents=documents, metadatas=metadatas)
    print(f"Inserted {len(records)} documents into the '{COLLECTION_NAME}' collection.")


def display_results(results) -> None:
    """Pretty-print the top-k query results."""
    ids = results.get("ids", [[]])[0]
    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    distances = results.get("distances", [[]])[0]
    # print(documents, metadatas, distances)

    if not documents:
        print("No results found.")
        return

    for rank, (doc_id, doc, meta, dist) in enumerate(zip(ids, documents, metadatas, distances), start=1):
        print(f"\nResult {rank}")
        print(f"  ID:       {doc_id}")
        print(f"  Text:     {doc}")
        print(f"  Source:   {meta.get('source', 'unknown')}")
        print(f"  Category: {meta.get('category', 'unknown')}")
        print(f"  Distance: {dist:.4f}")


def search_loop(collection) -> None:
    """Repeatedly prompt the user for a query and show top-k results."""
    print("\nCourse Knowledge Search Engine")
    print("Type a question to search the knowledge base, or 'exit' to quit.\n")

    while True:
        query = input("Query> ").strip()

        if query.lower() == "exit":
            print("Goodbye!")
            break

        if not query:
            print("Input cannot be empty. Please type a question, or 'exit' to quit.")
            continue

        # Chroma's default distance metric is squared L2 (Euclidean)
        # squared_L2_distance = 2 - 2 × cosine_similarity
        # If vectors are identical (cosine similarity = 1) → distance = 0
        # If vectors are unrelated (cosine similarity = 0) → distance = 2
        # If vectors are opposite (cosine similarity = -1) → distance = 4
        results = collection.query(query_texts=[query], n_results=TOP_K)
        display_results(results)
        print()


def main():
    records = load_knowledge_base(KNOWLEDGE_BASE_FILE)
    collection = get_collection()
    populate_collection(collection, records)
    search_loop(collection)


if __name__ == "__main__":
    main()