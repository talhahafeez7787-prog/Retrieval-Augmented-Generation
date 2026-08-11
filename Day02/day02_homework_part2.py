# -------------------------------------------------------------
# 1. Initializing values (title, source filename, paragraph)
# -------------------------------------------------------------
title = "AI in Practice"
source = "sample_source.txt"
text = "  Python is a great language for AI. python makes it easy to build RAG pipelines, and learning python is fun! Do you enjoy coding in python?  "

# -------------------------------------------------------------
# 2. Clean the text
#    - remove leading/trailing spaces
#    - convert to lowercase
#    - remove periods, commas, exclamation marks, question marks
# -------------------------------------------------------------
cleaned_text = text.strip().lower().replace(".", "").replace(",", "").replace("!", "").replace("?", "")

# -------------------------------------------------------------
# 3. Split into words and gather basic stats
# -------------------------------------------------------------
words = cleaned_text.split()

char_count = len(cleaned_text)
word_count = len(words)
first_word = words[0]
final_word = words[-1]
python_count = words.count("python")

# -------------------------------------------------------------
# 4. Create three chunks using slicing, then join each chunk
#    back into a string using join()
# -------------------------------------------------------------
chunk_size = word_count // 3  # roughly equal-sized chunks

chunk1_words = words[0:chunk_size]
chunk2_words = words[chunk_size:chunk_size * 2]
chunk3_words = words[chunk_size * 2:word_count]  # remainder goes in last chunk

chunk1_text = " ".join(chunk1_words)
chunk2_text = " ".join(chunk2_words)
chunk3_text = " ".join(chunk3_words)

# store the three chunk strings in a list
chunk_texts = [chunk1_text, chunk2_text, chunk3_text]

# -------------------------------------------------------------
# 5. Build metadata: one document dictionary + three chunk
#    dictionaries (chunk_id, text, source, title), stored in a list
# -------------------------------------------------------------
document = {
    "title": title,
    "source": source,
    "full_text": cleaned_text,
    "word_count": word_count,
}

chunk1_dict = {
    "chunk_id": 1,
    "text": chunk1_text,
    "source": source,
    "title": title,
}

chunk2_dict = {
    "chunk_id": 2,
    "text": chunk2_text,
    "source": source,
    "title": title,
}

chunk3_dict = {
    "chunk_id": 3,
    "text": chunk3_text,
    "source": source,
    "title": title,
}

chunks = [chunk1_dict, chunk2_dict, chunk3_dict]

# -------------------------------------------------------------
# 6. Display results
# -------------------------------------------------------------
print("\n----- CLEANED TEXT -----")
print(cleaned_text)

print("\n----- BASIC STATS -----")
print("Character count:", char_count)
print("Word count:", word_count)
print("First word:", first_word)
print("Final word:", final_word)
print("Occurrences of 'python':", python_count)

print("\n----- DOCUMENT METADATA -----")
print(document)

print("\n----- CHUNKS -----")
print("Total number of chunks:", len(chunks))

print("\nChunk 1:")
print("  Title :", chunk1_dict["title"])
print("  Source:", chunk1_dict["source"])
print("  Text  :", chunk1_dict["text"])

print("\nChunk 2:")
print("  Title :", chunk2_dict["title"])
print("  Source:", chunk2_dict["source"])
print("  Text  :", chunk2_dict["text"])

print("\nChunk 3:")
print("  Title :", chunk3_dict["title"])
print("  Source:", chunk3_dict["source"])
print("  Text  :", chunk3_dict["text"])