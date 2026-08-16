# Multi-File Keyword Search Tool

A command-line application that searches a user-provided keyword across every
`.txt` file in the `documents/` folder, displays structured results, saves
them to a results file, handles errors safely, and organizes the code into
reusable modules.

## Project Structure

```
keyword_search_project/
├── main.py                  # Command-line controller
├── text_utils.py             # Keyword cleaning, validation, matching
├── file_utils.py              # Folder/file scanning, searching, saving
├── documents/                # Sample .txt files to search
│   ├── python.txt
│   ├── rag.txt
│   └── ai.txt
├── results/
│   └── search_results.txt    # Generated after each search
├── requirements.txt
└── README.md
```

## Features

- Accepts a keyword from the user (or `exit` to quit).
- Cleans whitespace and performs case-insensitive matching.
- Rejects empty keywords.
- Verifies the `documents/` folder exists before searching.
- Reads only `.txt` files, line by line, ignoring empty lines.
- Displays filename, matching line number, and matching text.
- Counts matching files and total matches.
- Stores each match as a dictionary (`filename`, `line_number`, `text`).
- Creates the `results/` folder automatically if missing.
- Saves the keyword, timestamp, results, and totals to
  `results/search_results.txt`.
- Handles missing folders, permission errors, encoding errors, and any
  other unexpected exceptions without crashing.

## How It Works

- **`text_utils.py`** — pure text-processing functions with no file or
  terminal I/O: `prepare_keyword()`, `is_valid_keyword()`,
  `contains_keyword()` (plus an optional `contains_exact_word()` for
  whole-word matching).
- **`file_utils.py`** — handles the filesystem: `get_text_files()` finds
  valid `.txt` files, `search_file()` searches a single file,
  `search_folder()` searches every file and gracefully skips files with
  permission or encoding problems, `count_matching_files()` counts unique
  files with a match, and `save_results()` writes the summary and results
  to disk.
- **`main.py`** — the command-line loop: takes input, validates it, calls
  the search, displays results, saves them, and handles top-level errors
  (missing `documents/` folder, permission issues, anything unexpected).

## Setup

1. (Optional but recommended) Create and activate a virtual environment:

   ```bash
   python -m venv venv

   # Windows Command Prompt
   venv\Scripts\activate

   # Windows PowerShell
   venv\Scripts\Activate.ps1

   # macOS/Linux
   source venv/bin/activate
   ```

2. No external packages are required — see `requirements.txt`. If you add
   any dependencies later, install them with:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the tool from the project root:

```bash
python main.py
```

Example session:

```
=== Multi-File Keyword Search Tool ===
Type 'exit' to close the program.

Enter a keyword: python

Files checked: 3

Search results:
1. ai.txt | Line 6
   Python provides many tools for AI development.
2. python.txt | Line 1
   Python is a beginner-friendly programming language.
...

Matching files: 3
Total matches: 6

Results saved to: results/search_results.txt

Enter a keyword: exit
Search tool closed.
```

Each search overwrites `results/search_results.txt` with the keyword,
timestamp, totals, and full result list.

## Notes

- Matching is **substring-based** and case-insensitive, so searching `rag`
  will also match longer words that contain those letters (e.g. "fragrant").
  An optional `contains_exact_word()` function in `text_utils.py` is
  provided for whole-word matching if you want to extend the project.
- This project intentionally keeps document loading, matching, and output
  simple (plain-text keyword search) so it can later be extended toward a
  Retrieval-Augmented Generation (RAG) pipeline — e.g. swapping keyword
  matching for embedding-based semantic search while keeping the same
  patterns: loading documents, keeping source metadata, modular code,
  structured results, and graceful error handling.
