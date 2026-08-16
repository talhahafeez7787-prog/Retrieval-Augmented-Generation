# text_utils.py
"""Utility functions for keyword cleaning, validation, and matching.

This module contains no terminal input and no direct file handling.
"""


def prepare_keyword(keyword):
    """Return a cleaned, lowercase keyword."""
    return keyword.strip().lower()


def is_valid_keyword(keyword):
    """Return True when the keyword is not empty."""
    return len(keyword) > 0


def contains_keyword(text, keyword):
    """Perform a case-insensitive substring search."""
    return keyword in text.lower()


def contains_exact_word(text, keyword):
    """Optional bonus: perform an exact whole-word search."""
    clean_text = text.lower()
    clean_text = clean_text.replace('.', '').replace(',', '')
    words = clean_text.split()
    return keyword in words


if __name__ == '__main__':
    sample_keyword = prepare_keyword(' PYTHON ')
    sample_text = 'Python is used for RAG.'
    print(sample_keyword)
    print(is_valid_keyword(sample_keyword))
    print(contains_keyword(sample_text, sample_keyword))
