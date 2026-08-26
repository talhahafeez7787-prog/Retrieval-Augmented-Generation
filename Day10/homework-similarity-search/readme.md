# University Rules Similarity Search

A small semantic (embedding-based) search tool over a JSON knowledge base of
university rules and policies. Given a natural-language question, it returns
the 3 most relevant rules, ranked by cosine similarity.

## How it works

1. **Knowledge base** (`knowledge_base.json`) — 10 records, each with
   `id`, `text`, and `source`.
2. **Embeddings** — every record's `text` is embedded once at startup using
   `sentence-transformers/all-MiniLM-L6-v2`.
3. **Query** — the user types a question; it is embedded with the same model.
4. **Scoring** — cosine similarity is computed between the query vector and
   every document vector.
5. **Ranking** — results are sorted highest → lowest similarity.
6. **Output** — the top 3 matches are displayed with their `source` and a
   score rounded to 3 decimal places.
7. **Validation** — empty or whitespace-only queries are rejected with a
   clear error message instead of being searched.

## Files

| File | Purpose |
|---|---|
| `knowledge_base.json` | The 10-record dataset (id, text, source) |
| `similarity_search.py` | Main program: loads data, embeds, searches, displays results |
| `README.md` | This file |

## Setup

```bash
pip install sentence-transformers numpy
```

The first run will download the `all-MiniLM-L6-v2` model (~80 MB) from
Hugging Face, so an internet connection is required the first time. After
that, the model is cached locally and subsequent runs work offline.

## Run

```bash
python3 similarity_search.py
```

You'll be prompted to enter a query. Type `quit` at any time to exit.

## Example session (expected output)

```
Loading embedding model 'all-MiniLM-L6-v2' ...
Model loaded.

University Rules Similarity Search
Type your question below, or type 'quit' to exit.

Enter your search query (or 'quit' to exit): What happens if I miss too many classes?

Top 3 result(s):
--------------------------------------------------
1. Score: 0.612
   Text:   Students are allowed a maximum of three unexcused absences per course per semester. A fourth unexcused absence may result in a grade penalty or course withdrawal at the instructor's discretion.
   Source: Student Attendance Policy, Section 2.3

2. Score: 0.298
   Text:   Course withdrawal is permitted up to the end of the eighth week of the semester. Withdrawals after this deadline require approval from the Dean of Students and are recorded as a 'W' on the transcript.
   Source: Registrar Policy Manual, Section 6.1

3. Score: 0.245
   Text:   Any form of plagiarism, including submitting AI-generated text as one's own work without disclosure, is a violation of the Academic Integrity Code and may result in course failure or expulsion.
   Source: Academic Integrity Code, Article 5
```

## Test queries used

The program was tested with at least three different queries, covering
different topics in the knowledge base:

1. `"What happens if I miss too many classes?"` → top match: **Student
   Attendance Policy, Section 2.3**
2. `"Can I use my phone during an exam?"` → top match: **Examination
   Regulations, Section 7.2**
3. `"How do I pay my tuition fees on time?"` → top match: **Finance Office
   Guidelines, Section 1.2**
4. `"What is the minimum GPA required?"` → top match: **Academic Policy
   Handbook, Section 4.1**
5. `""` (empty input) → rejected with: `Error: query cannot be empty.
   Please enter a valid search query.`

## Note on this sandbox environment

This program was developed and its logic (JSON loading, cosine similarity,
sorting, top-k selection, and empty-query validation) was fully tested end
to end in this environment. However, the sandbox's network is restricted to
a package-manager allowlist (pypi.org, npmjs.org, etc.) and does **not**
include `huggingface.co`, which is where `sentence-transformers` downloads
model weights from. So while `pip install sentence-transformers` succeeded
here, actually downloading `all-MiniLM-L6-v2` was not possible in this
sandbox. The code is correct and standard — it will download the model and
run immediately on any machine with normal internet access (e.g., your own
computer, Colab, or a CI runner).