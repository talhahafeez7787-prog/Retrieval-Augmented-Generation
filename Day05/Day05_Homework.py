"""
Safe Document Search and Report Generator
Applied RAG Engineering - Week 2, Day 2: File Handling and Error Handling

Reads a text file, searches every non-empty line for a keyword
(case-insensitive), reports every matching line with its original
line number, counts matches and exact keyword occurrences, saves a
full report to search_results.txt, and appends a one-line summary
to search_history.txt.
"""

import os
from datetime import datetime

REPORT_FILE = "search_results.txt"
HISTORY_FILE = "search_history.txt"


# ---------------------------------------------------------------------
# Week 2 Day 1 style helper functions
# ---------------------------------------------------------------------

def clean_line(line):
    """
    Clean a single line of text.

    Strips leading/trailing whitespace (including the trailing newline).
    Returns the cleaned string, which will be an empty string "" if the
    line was blank.
    """
    return line.strip()


def search_lines(lines, keyword):
    """
    Search a list of raw lines for a keyword (case-insensitive).

    - Uses clean_line() to clean each line and skips empty lines.
    - Records every matching line together with its ORIGINAL line number
      (1-based, based on position in the original file).
    - Counts both the number of matching lines and the total number of
      exact keyword occurrences across all matching lines.

    Returns a tuple:
        (matches, total_matching_lines, total_occurrences)
    where matches is a list of (line_number, line_text, occurrences_in_line)
    """
    matches = []
    total_occurrences = 0
    keyword_lower = keyword.lower()

    for index, raw_line in enumerate(lines, start=1):
        cleaned = clean_line(raw_line)

        if cleaned == "":
            # Ignore empty lines
            continue

        cleaned_lower = cleaned.lower()
        occurrences_in_line = cleaned_lower.count(keyword_lower)

        if occurrences_in_line > 0:
            matches.append((index, cleaned, occurrences_in_line))
            total_occurrences += occurrences_in_line

    return matches, len(matches), total_occurrences


def save_results(source_filename, keyword, matches, total_matches, total_occurrences):
    """
    Save a complete report of a search to REPORT_FILE.

    Bonus behaviour: uses 'x' mode to CREATE the report file only if it
    does not already exist (so the file is created fresh the very first
    time). On every later call, since the file now exists, it switches
    to append ('a') mode so that new reports are added to the file
    instead of overwriting previous ones.

    Every saved report includes the source filename and the keyword
    that was searched for.
    """
    file_is_new = not os.path.exists(REPORT_FILE)

    try:
        if file_is_new:
            report_handle = open(REPORT_FILE, "x", encoding="utf-8")
        else:
            report_handle = open(REPORT_FILE, "a", encoding="utf-8")

        with report_handle as report_file:
            report_file.write("=" * 60 + "\n")
            report_file.write(f"Search performed : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            report_file.write(f"Source file      : {source_filename}\n")
            report_file.write(f"Keyword          : {keyword}\n")
            report_file.write(f"Matching lines   : {total_matches}\n")
            report_file.write(f"Total occurrences: {total_occurrences}\n")
            report_file.write("-" * 60 + "\n")

            if total_matches == 0:
                report_file.write("No result found\n")
            else:
                for line_number, line_text, occurrences_in_line in matches:
                    report_file.write(
                        f"Line {line_number} ({occurrences_in_line} match(es)): {line_text}\n"
                    )

            report_file.write("=" * 60 + "\n\n")

    except PermissionError:
        print(f"Error: permission denied while writing to '{REPORT_FILE}'.")
    except Exception as error:
        print(f"Unexpected error while saving the report: {error}")


def append_history(source_filename, keyword, total_matches, total_occurrences):
    """
    Append a single one-line summary of the search to HISTORY_FILE.
    Uses append ('a') mode, which creates the file automatically if it
    does not yet exist.
    """
    try:
        with open(HISTORY_FILE, "a", encoding="utf-8") as history_file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            history_file.write(
                f"[{timestamp}] file='{source_filename}' keyword='{keyword}' "
                f"matching_lines={total_matches} occurrences={total_occurrences}\n"
            )
    except PermissionError:
        print(f"Error: permission denied while writing to '{HISTORY_FILE}'.")
    except Exception as error:
        print(f"Unexpected error while writing to history: {error}")


# ---------------------------------------------------------------------
# Input helpers
# ---------------------------------------------------------------------

def get_nonempty_input(prompt):
    """
    Ask the user for input and reject empty values.
    Returns the stripped, non-empty string the user entered, or the
    special value "exit" if the user wants to quit.
    """
    while True:
        value = input(prompt).strip()

        if value.lower() == "exit":
            return "exit"

        if value == "":
            print("Input cannot be empty. Please try again (or type 'exit' to quit).")
            continue

        return value


# ---------------------------------------------------------------------
# Core workflow
# ---------------------------------------------------------------------

def read_file_lines(filename):
    """
    Read all lines from filename using UTF-8 encoding.
    Returns the list of lines, or None if an error occurred
    (the specific error is already printed to the user).
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.readlines()

    except FileNotFoundError:
        print(f"Error: the file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: you do not have permission to read '{filename}'.")
    except UnicodeDecodeError:
        print(f"Error: '{filename}' could not be decoded as UTF-8 text.")
    except Exception as error:
        print(f"An unexpected error occurred while reading '{filename}': {error}")

    return None


def run_single_search():
    """
    Run one full search cycle: ask for filename and keyword, search,
    display results, and save the report/history.
    Returns "exit" if the user chose to quit, otherwise None.
    """
    filename = get_nonempty_input("Enter the input filename (or 'exit' to quit): ")
    if filename == "exit":
        return "exit"

    keyword = get_nonempty_input("Enter the keyword to search for (or 'exit' to quit): ")
    if keyword == "exit":
        return "exit"

    lines = read_file_lines(filename)
    if lines is None:
        # Error already reported by read_file_lines
        return None

    matches, total_matches, total_occurrences = search_lines(lines, keyword)

    print(f"\nSearching '{filename}' for keyword '{keyword}' (case-insensitive)...\n")

    if total_matches == 0:
        print("No result found")
    else:
        for line_number, line_text, occurrences_in_line in matches:
            print(f"Line {line_number} ({occurrences_in_line} match): {line_text}")

        print(f"\nTotal matching lines : {total_matches}")
        print(f"Total occurrences    : {total_occurrences}")

    save_results(filename, keyword, matches, total_matches, total_occurrences)
    append_history(filename, keyword, total_matches, total_occurrences)

    print(f"\nFull report saved to '{REPORT_FILE}'.")
    print(f"Summary appended to '{HISTORY_FILE}'.\n")

    return None


def main():
    print("=== Safe Document Search and Report Generator ===")
    print("Type 'exit' at any prompt to stop.\n")

    while True:
        result = run_single_search()
        if result == "exit":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()