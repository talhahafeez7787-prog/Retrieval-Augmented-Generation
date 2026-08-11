"""
Applied RAG Engineering - Week 1, Day 3
Conditionals and Loops 101

A command-line keyword search tool over a small corpus of sentences
related to Python, AI, RAG, embeddings, documents, and vector databases.

No functions and no regular expressions are used - everything runs
top to bottom using only loops, conditionals, and plain string methods.
"""

import string

# ---------------------------------------------------------------------------
# Corpus: each sentence is stored as a dictionary with text + metadata
# (this satisfies the "store each sentence as a dict with source/page" bonus)
# ---------------------------------------------------------------------------
sentence_corpus = [
    {"text": "Python is a popular language for building AI applications.", "source": "intro.md", "page": 1},
    {"text": "RAG stands for Retrieval-Augmented Generation.", "source": "rag_basics.md", "page": 1},
    {"text": "Embeddings convert text into numerical vectors.", "source": "embeddings.md", "page": 2},
    {"text": "A vector database stores embeddings for fast similarity search.", "source": "vector_db.md", "page": 1},
    {"text": "Documents are chunked before being converted into embeddings.", "source": "documents.md", "page": 3},
    {"text": "Python libraries like NumPy help with vector math in AI pipelines.", "source": "intro.md", "page": 2},
    {"text": "RAG systems combine retrieval with a language model for generation.", "source": "rag_basics.md", "page": 2},
    {"text": "Cosine similarity is often used to compare embeddings in a vector database.", "source": "vector_db.md", "page": 2},
    {"text": "Good document preprocessing improves the quality of AI retrieval.", "source": "documents.md", "page": 1},
    {"text": "Many AI frameworks are written in Python for rapid prototyping.", "source": "intro.md", "page": 3},
    {"text": "Indexing embeddings in a vector database enables scalable RAG pipelines.", "source": "vector_db.md", "page": 3},
    {"text": "Splitting documents into smaller chunks helps embeddings capture context.", "source": "documents.md", "page": 2},
]

print("=" * 60)
print(" Keyword Search over RAG / AI / Embeddings Sentences")
print(" Type a keyword to search, or type 'exit' to quit.")
print("=" * 60)

search_round = 0  # counts how many searches the user has performed

# 'while' loop: keep asking for keywords until the user exits
while True:
    raw_input_text = input("\nEnter a keyword to search: ")

    # Normalize: strip outer spaces, collapse internal whitespace, lowercase.
    # split() with no argument breaks on any run of whitespace and drops
    # empty pieces, so join(split()) is a regex-free way to collapse spaces.
    cleaned_keyword = " ".join(raw_input_text.split())
    keyword = cleaned_keyword.lower()

    # Exit condition
    if keyword == "exit":
        print("Goodbye!")
        break  # stop the while loop entirely

    # Input validation: reject empty input after normalization
    if keyword == "":
        print("Input cannot be empty. Please enter a real keyword.")
        continue  # skip the rest of this loop iteration, ask again

    search_round += 1
    matching_sentences = []   # new list to hold matches for this search
    total_occurrences = 0     # counts every occurrence of the keyword, not just sentences

    # Split the keyword itself into words, so "AI and RAG" becomes
    # ["ai", "and", "rag"]. This lets us support both single-word and
    # multi-word (phrase) searches with the same logic below.
    # Punctuation is stripped from each keyword word too, so a keyword
    # typed as "often used!" still matches sentence text "often used".
    raw_keyword_words = keyword.split()
    keyword_words = []
    for raw_keyword_word in raw_keyword_words:
        keyword_words.append(raw_keyword_word.strip(string.punctuation))
    keyword_length = len(keyword_words)

    # print(keyword_words)

    # 'for' loop: walk through every sentence, tracking its original position
    for index, entry in enumerate(sentence_corpus):
        sentence_text = entry["text"]

        # Strip punctuation from each word so "AI." and "AI" both match "ai"
        raw_words = sentence_text.lower().split()
        words_in_sentence = []
        for raw_word in raw_words:
            clean_word = raw_word.strip(string.punctuation)
            words_in_sentence.append(clean_word)

        occurrences_here = 0

        # Slide a window the same length as keyword_words across the
        # sentence's words, checking for a consecutive, in-order match.
        # This works for a single word (window size 1) and for phrases
        # like "ai and rag" (window size 3) using the same code.
        window_start = 0
        while window_start <= len(words_in_sentence) - keyword_length:
            window = words_in_sentence[window_start:window_start + keyword_length]
            if window == keyword_words:
                occurrences_here += 1
            window_start += 1

        if occurrences_here == 0:
            # no match in this sentence, move on to the next one
            continue

        total_occurrences += occurrences_here
        matching_sentences.append({
            "position": index + 1,          # 1-based original position in corpus
            "text": sentence_text,
            "source": entry["source"],
            "page": entry["page"],
        })

    # Decide what to show based on whether we found anything
    if len(matching_sentences) == 0:
        print("No result found.")
    else:
        print(f"\n--- Matches for '{keyword}' ---")
        result_number = 1
        for match in matching_sentences:
            print(f"{result_number}. [Position {match['position']}] "
                  f"(source: {match['source']}, page: {match['page']}) -> {match['text']}")
            result_number += 1

        print(f"\nTotal matching sentences: {len(matching_sentences)}")
        print(f"Total keyword occurrences: {total_occurrences}")
        print(f"First match: {matching_sentences[0]['text']}")
        print(f"Last match: {matching_sentences[-1]['text']}")

        # Bonus: optionally filter the current matches by source or page
        filter_choice = input("Filter these results by source or page? (y/n): ").strip().lower()

        if filter_choice == "y":
            filter_type = input("Filter by 'source' or 'page': ").strip().lower()
            filtered_sentences = []

            if filter_type == "source":
                source_query = input("Enter source name to filter by: ").strip().lower()
                for match in matching_sentences:
                    if match["source"].lower() == source_query:
                        filtered_sentences.append(match)
            elif filter_type == "page":
                page_query = input("Enter page number to filter by: ").strip()
                if page_query.isdigit():
                    for match in matching_sentences:
                        if match["page"] == int(page_query):
                            filtered_sentences.append(match)
                else:
                    print("Page number must be numeric.")
            else:
                print("Unrecognized filter type. Skipping filter.")

            if len(filtered_sentences) == 0:
                print("No result found.")
            else:
                print("\n--- Filtered Results ---")
                filtered_number = 1
                for match in filtered_sentences:
                    print(f"{filtered_number}. [Position {match['position']}] "
                          f"(source: {match['source']}, page: {match['page']}) -> {match['text']}")
                    filtered_number += 1
        else:
            pass  # user chose not to filter, nothing else to do

print(f"Session ended after {search_round} search(es). Thanks for using the tool!")