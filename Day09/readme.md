# Sentence Embeddings Demo

A small project that loads a set of sentence records, generates embeddings
for them using the `all-MiniLM-L6-v2` sentence-transformer model, and prints
the resulting embedding details.

## Project structure

```
sentence-embeddings-demo/
├── main.py             # Loads data, generates embeddings, prints results
├── sentences.json       # 9 sentence records across 3 topics
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

## Data

`sentences.json` contains 9 records spread across 3 topics:

- **technology** (3 records)
- **nature** (3 records)
- **sports** (3 records)

Each record has the shape:

```json
{
  "id": 1,
  "topic": "technology",
  "text": "Artificial intelligence is transforming how software is built and deployed."
}
```

## Setup

1. **(Recommended) Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   > Note: The first run will also download the `all-MiniLM-L6-v2` model
   > weights (a few hundred MB) from Hugging Face, so an internet connection
   > is required the first time you run the script.

## Run

From the project directory, run:

```bash
python main.py
```

## Expected output

The script will:

1. Load all sentence records from `sentences.json`.
2. Load the `all-MiniLM-L6-v2` model.
3. Generate embeddings for all sentences at once.
4. Print the **complete embeddings shape**, e.g.:

   ```
   Embeddings shape: (9, 384)
   ```

5. For **every record**, print:
   - The sentence text
   - Its topic
   - The embedding dimension (384 for this model)
   - The first five values of its embedding vector

   Example:

   ```
   Text: Artificial intelligence is transforming how software is built and deployed.
   Topic: technology
   Dimension: 384
   First 5 values: [0.0123, -0.0456, 0.0789, 0.0012, -0.0345]
   ------------------------------------------------------------
   ```

## Model notes

- **Model:** `all-MiniLM-L6-v2` (via the `sentence-transformers` library)
- **Embedding dimension:** 384
- The model maps sentences to a dense vector space where semantically
  similar sentences are located close to one another, which is useful for
  tasks like semantic search, clustering, and similarity comparison.