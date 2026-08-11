print("=== Document Information System ===")
# User input
title = input("Enter document title: ")
pages = int(input("Enter number of pages: "))
file_size = float(input("Enter file size in MB: "))
# Collections
keywords = ["python", "rag", "documents", "retrieval", "ai"]
supported_formats = ("pdf", "docx", "txt")
unique_topics = {"python", "rag", "retrieval", "python"}
# Dictionary containing all document information
document = {
 "title": title,
 "pages": pages,
 "file_size_mb": file_size,
 "processed": False,
 "keywords": keywords
}


print("\n=== Document Details ===")
print("Title:", document["title"])
print("Pages:", document["pages"])
print("File size:", document["file_size_mb"], "MB")
print("Processed:", document["processed"])
print("Keywords:", document["keywords"])
print("Supported formats:", supported_formats)
print("Unique topics:", unique_topics)
print("\n=== Types ===")
print("Title type:", type(title))
print("Pages type:", type(pages))
print("File size type:", type(file_size))
print("Keywords type:", type(keywords))
print("Formats type:", type(supported_formats))
print("Topics type:", type(unique_topics))
print("Document type:", type(document))


print("\n=== Lengths ===")
print("Title characters:", len(title))
print("Total keywords:", len(keywords))
print("Total formats:", len(supported_formats))
print("Total unique topics:", len(unique_topics))
print("Document fields:", len(document))