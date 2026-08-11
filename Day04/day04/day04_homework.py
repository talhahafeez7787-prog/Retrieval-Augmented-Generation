"""
Applied RAG Engineering · Week 2, Day 1: Functions in Python
Homework: Analyze and search a list of AI/RAG-related sentences.
"""

# ---------------------------------------------------------------------------
# Data: at least 10 AI/RAG-related sentences
# ---------------------------------------------------------------------------
SENTENCES = [
    "Retrieval-Augmented Generation combines a retriever with a language model.",
    "A vector database stores embeddings for fast similarity search.",
    "Chunking documents properly improves retrieval quality in RAG pipelines.",
    "Large language models can hallucinate facts without grounded context.",
    "Embeddings map text into a high-dimensional vector space.",
    "A reranker can refine the top results returned by a retriever.",
    "Prompt engineering shapes how a language model responds to a query.",
    "Fine-tuning adapts a pretrained model to a specific task or domain.",
    "Semantic search relies on vector similarity rather than keyword matching.",
    "An agent can call external tools to complete complex tasks.",
    "Context windows limit how much text a language model can process at once.",
    "Indexing strategies affect both retrieval speed and search accuracy.",
]


# ---------------------------------------------------------------------------
# Processing functions
# ---------------------------------------------------------------------------
def clean_text(text, lowercase=True):
    """
    Clean a piece of text by stripping whitespace and (optionally) lowercasing it.
    Uses a default parameter: lowercase=True.
    """
    cleaned = text.strip()
    if lowercase:
        cleaned = cleaned.lower()
    return cleaned


def count_words(text):
    """Return the number of words in a piece of text."""
    cleaned = clean_text(text, lowercase=False)  # keyword argument used here
    if not cleaned:
        return 0
    return len(cleaned.split())


def count_keyword(text, keyword):
    """Return how many times keyword appears in text (case-insensitive)."""
    clean_sentence = clean_text(text)
    clean_kw = clean_text(keyword)
    if not clean_kw:
        return 0
    return clean_sentence.count(clean_kw)


def search_sentences(sentences, keyword):
    """
    Search a list of sentences for a keyword (case-insensitive).
    Returns a list of dicts describing each match instead of printing directly.
    """
    clean_kw = clean_text(keyword)
    results = []

    if not clean_kw:
        # Reject empty keyword
        return results

    for index, sentence in enumerate(sentences, start=1):
        if clean_kw in clean_text(sentence):
            results.append({
                "number": index,
                "sentence": sentence,
                "word_count": count_words(sentence),
                "keyword_count": count_keyword(sentence, clean_kw),
            })

    return results


# ---------------------------------------------------------------------------
# Display function
# ---------------------------------------------------------------------------
def display_results(results, keyword=""):
    """Print the search results in a readable format."""
    if not results:
        print("No result found")
        return

    print(f"\nResults for keyword: '{keyword}'\n" + "-" * 40)
    for item in results:
        print(f"Sentence #{item['number']}: {item['sentence']}")
        print(f"  Word count: {item['word_count']}")
        print(f"  Keyword occurrences: {item['keyword_count']}\n")

    print(f"Total matches: {len(results)}")


# ---------------------------------------------------------------------------
# Main program
# ---------------------------------------------------------------------------
def main():
    keyword = input("Enter a keyword to search for: ")

    if not clean_text(keyword):
        print("Error: keyword cannot be empty.")
        return

    # Call using a keyword argument
    results = search_sentences(SENTENCES, keyword=keyword)

    # Call using a keyword argument
    display_results(results, keyword=keyword)


if __name__ == "__main__":
    main()