#Exercise 1
text = "Retrieval"
# Complete the following:
# 1. Print the first character.
print(text[0])
# 2. Print the last character.
print(text[-1])
# 3. Print "trie" using slicing.
print(text[2:6])
# 4. Reverse the string.
print(text[::-1])
# 5. Print the total number of characters.
print(len(text))


#Exercise 2
text = " PYTHON, RAG, and AI are useful! "
# Clean the text so the final result is:
# python rag and ai are useful
clean_text = text.strip().lower().replace(",", "").replace("!", "")
print(clean_text)
# Then print the word count.
words = clean_text.split()
print(len(words))


#Exercise 3
tools = ["Python", "LangChain"]
# 1. Add "ChromaDB" to the end.
tools.append("ChromaDB")
# 2. Insert "Hugging Face" at index 1.
tools.insert(1, "Hugging Face")
# 3. Add "FastAPI" and "Streamlit" using one method.
tools.extend(["FastAPI", "Streamlit"])
# 4. Remove "LangChain".
tools.remove("LangChain")
# 5. Print the final list and its length.
print(tools)
print(len(tools))


#Exercise 4
document = {
 "title": "RAG Notes",
 "pages": 12,
 "processed": False
}
# 1. Print the title.
print(document["title"])
# 2. Add source = "rag_notes.pdf".
document["source"] = "rag_notes.pdf"
# 3. Change processed to True.
document["processed"] = True
# 4. Add keywords = ["rag", "retrieval", "llm"].
document["keywords"] = ["rag", "retrieval", "llm"]
# 5. Print the number of dictionary fields.
print(len(document))
# 6. Print the second keyword.
print(document["keywords"][1])


#Exercise 5
text = "Python helps developers build practical AI systems with document processing APIs and retrieval pipelines"
# 1. Convert the text to lowercase.
text = text.lower()
# 2. Split it into words.
words = text.split()
# 3. Create three chunks using slices 0:5, 5:10, and 10:.
chunk_1_words_list = words[0:5]
chunk_2_words_list = words[5:10]
chunk_3_words_list = words[10:]
# 4. Join each chunk back into text.
chunk_1 = " ".join(chunk_1_words_list)
chunk_2 = " ".join(chunk_2_words_list)
chunk_3 = " ".join(chunk_3_words_list)
# 5. Store the chunks in a list.
chunks = [chunk_1, chunk_2, chunk_3]
# 6. Store the first chunk in a dictionary with source and chunk_id.
chunk_record = {
    "chunk_id" : 1,
    "text" : chunks[0],
    "source" : "class_notes.txt"
}
print(chunks)
print(chunk_record)