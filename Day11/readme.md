# Course Knowledge Search Engine

A small semantic search engine for course notes, built with a persistent
ChromaDB collection. Course content lives in `knowledge_base.json`; running
`main.py` embeds that content into a local vector database and lets you
search it with plain-English questions from an interactive command-line loop.

## Project structure

```
course-knowledge-search/
├── main.py              # Loads data, builds the collection, runs the search loop
├── knowledge_base.json  # 12 course records across 3 categories
├── requirements.txt     # Python dependencies
├── README.md            # This file
├── .gitignore           # Excludes chroma_db/ and other local artifacts
└── chroma_db/           # Generated on first run (not submitted, safe to delete)
```

## Knowledge base

`knowledge_base.json` contains 12 records, each with a unique `id`, the
`text` of the note, a `source` file name, and a `category`. The records span
three categories:

- **LLM Fundamentals** – embeddings, RAG, prompt engineering, fine-tuning,
  transformers, LLM evaluation
- **Vector Search & Embeddings** – vector databases, cosine similarity,
  chunking
- **Software Engineering** – Git, unit testing, Docker

## Setup

1. Create and activate a virtual environment (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   Note: the first time the script runs, ChromaDB will download its default
   embedding model (`all-MiniLM-L6-v2`) from the internet. This requires a
   working internet connection on first run only; after that the model is
   cached locally.

## Running the search engine

```bash
python main.py
```

On first run, the script reads `knowledge_base.json`, creates a persistent
ChromaDB collection in `./chroma_db/`, and embeds and inserts all 12 records.
On later runs, it detects the existing collection and skips re-inserting.

You'll then see a prompt:

```
Query>
```

Type a natural-language question and press Enter to see the top 3 matching
results, each showing the document text, source file, category, and
similarity distance (lower distance = more similar). Type `exit` to quit.
Pressing Enter with no text is rejected and re-prompts you.

## Test queries

Below are five example queries you can run against the knowledge base, along
with the top result you should expect to see.

1. **`what is a vector database`**
   Top result: *kb002* – "A vector database stores embeddings alongside
   their original content and metadata..." (Vector Search & Embeddings)

2. **`how do I keep my code changes organized with a team`**
   Top result: *kb008* – "Git version control lets teams track changes to
   code over time..." (Software Engineering)

3. **`how does an LLM decide which words to pay attention to`**
   Top result: *kb012* – "The transformer architecture relies on a
   self-attention mechanism..." (LLM Fundamentals)

4. **`why do we split documents into smaller pieces before embedding them`**
   Top result: *kb005* – "Chunking splits long documents into smaller
   passages before embedding them..." (Vector Search & Embeddings)

5. **`how can I package my app so it runs the same everywhere`**
   Top result: *kb010* – "Docker packages an application together with its
   dependencies into a portable container image..." (Software Engineering)

6. **`how do I know if my model's answers are actually good`**
   Top result: *kb011* – "Evaluating a language model's output quality
   often involves a mix of automated metrics..." (LLM Fundamentals)

## Input validation

- Empty input (just pressing Enter) is rejected with a message asking for a
  non-empty query, and the loop continues.
- Typing `exit` (case-insensitive) ends the program gracefully.