#2.2 Python Executes Instructions
print("First Instruction")
print("Second Instruction")
print("Third Instruction")


#2.3 Python Is Case-Sensitive
name = "Ali"
Name = "Sara"
print(name)
print(Name)


#4.2 Printing
print(100)
print(10 + 20)


#4.3 Comments
#This is a comment
print("Hello World")  # This is an inline comment
"""
This is a multiline comment
"""


#5.1 What a Variable Is
student_name = "Ali"
age = 22
course_fee = 30000
print(student_name)
print(age)
print(course_fee)


#5.2 Updating a Variable
score = 50
print(score)
score = 80
print(score)


#6.1 (1) String
name = "Talha"
course = 'RAG Engineering'
message = "Welcome to Python"
print(name)
print(course)
print(type(message))


#6.1 (2) String Concatenation and len()
first_name = "Talha"
last_name = "Hafeez"
full_name = first_name + " " + last_name
print(full_name)
title = "Python"
print(len(title))


#6.2 Integer Arithmetic
a = 16
b = 31
print(a + b) # addition
print(a - b) # subtraction
print(a * b) # multiplication
print(a // b) # whole-number division
print(a % b) # remainder
print(a ** b) # power


#6.3 Integer and Float Together
whole_number = 10
decimal_number = 2.5
result = whole_number + decimal_number #result becomes float
print(result)
print(type(result))


#6.4 Comparisons Produce Boolean Values
print(10 > 5)
print(10 == 5)
print("rag" == "rag")


#6.5 (1) List
tools = ["RAG", "AI", "Vector"]
print(tools)
print(type(tools))
print(len(tools))


#6.5 (2) Accessing, Updating, and Mixing List Items
tools = ["RAG", "AI", "Vector"]
print(tools[0])
tools[2] = "ChromaDB"
tools.append("FastAPI")
print(tools)


#6.6 Tuple
supported_formats = ("pdf", "docx", "txt")
print(supported_formats)
print(supported_formats[0])
print(len(supported_formats))


#6.7 (1) Set
keywords = {"python", "rag", "python", "ai", "rag"}
print(keywords)
print(len(keywords))


#6.7 (2) Adding and Removing Set Items
topics = {"python", "rag"}
topics.add("embeddings")
topics.remove("python")
print(topics)


#6.8 (1) Dictionary
document = {
 "title": "Introduction to RAG",
 "pages": 15,
 "processed": False
}
print(document)
print(type(document))
print(len(document))


#6.8 (2) Accessing, Adding, and Updating Values in Dictionary
print(document["title"])
print(document.get("pages"))
document["file_type"] = "pdf"
document["processed"] = True
print(document)


#7.2 Input
name = input("Enter your name: ")
print("Welcome", name)
print(type(name))


#7.3 Type
print(type("Python"))
print(type(25))
print(type(0.87))
print(type(True))
print(type([1, 2, 3]))
print(type({"name": "Ali"}))


#7.4 (1) len()
title = "Python"
keywords = ["python", "rag", "ai"]
formats = ("pdf", "docx", "txt")
unique_topics = {"rag", "ai"}
metadata = {"title": "RAG", "pages": 10}
print(len(title))
print(len(keywords))
print(len(formats))
print(len(unique_topics))
print(len(metadata))


#7.4 (2) len() with Numbers
number = 100
print(len(str(number)))


#8.1 str()
age = 22
message = "Age: " + str(age)
print(message)
print(type(str(age)))


#8.2 int()
age_text = "22"
age = int(age_text)
print(age + 1)
print(type(age))
age = int(input("Enter your age: "))
print("Next year you will be", age + 1)


#8.3 float()
file_size_text = "2.75"
file_size = float(file_size_text)
print(file_size)
print(type(file_size))


#8.4 bool()
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Python"))
print(bool([]))
print(bool(["RAG"]))