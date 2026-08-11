#===============PART-1===============
#Initialization of the student variables
name = "Talha"
age = 25
city = "Bahawalpur"
programming_languages = ["Java", "Python", "R"]
student_profile = {
    "name" : name,
    "age" : age
}

#Printing type
print(type(name))
print(type(age))
print(type(city))
print(type(programming_languages))
print(type(student_profile))

#Printing length
print(len(name))
print(len(city))
print(len(programming_languages))
print(len(student_profile))


#===============PART-2===============
#Initializing strings
first_name = "Ali"
last_name = 'Ahsan'
message = "This is a string with \"quotation mark\"."
multiline_message = '''This is a string
having
multiple lines.'''
error_message = '''Error\t404:\nThe page or item does not exist...
Check the file at C:\\programfiles\\vscode'''

#Printing strings
print(message)
print(multiline_message)
print(error_message)


#===============PART-3===============
text = 'Artificial Intelligence'
# First, last, and fifth character
print("First character:", text[0])
print("Last character:", text[-1])
print("Fifth character:", text[4])
# First 10 characters
print("First 10 chars:", text[:10])
# Index 11 to end
print("Index 11 to end:", text[11:])
# Every second character
print("Every second character:", text[::2])
# Reverse string
print("Reversed string:", text[::-1])
# Last valid index using len()
print("Last valid index:", len(text) - 1)


#===============PART-4===============
full_name = first_name + ' ' + last_name
course = "RAG Engineering"
semester = 6
print('=' * 30)
print(f"Student name: {full_name}\nCourse: {course}\nSemester: {semester}")
print("RAG" in course)
print("Java" not in course)


#===============PART-5===============
text = ' PYTHON, RAG, and AI are Useful! '
# lower
print("lower():", text.lower())
# upper
print("upper():", text.upper())
# title
print("title():", text.title())
# capitalize
print("capitalize():", text.capitalize())
# strip
print("strip():", text.strip())
# replace
print("replace('AI', 'Machine Learning'): ", text.replace('AI', 'Machine Learning'))
# remove commas
print("remove commas: ", text.replace(',', ''))
# split
print("split(): ", text.split())
# join (joining the split words back with a hyphen)
print("join('-'): ", '-'.join(text.split()))
# find('RAG')
print("find('RAG'): ", text.find('RAG'))
# count('AI')
print("count('AI'): ", text.count('AI'))
# startswith('PYTHON')  -> note: text has a leading space, so check both raw and stripped
print("startswith('PYTHON'): ", text.startswith('PYTHON'))
print("strip().startswith('PYTHON'):", text.strip().startswith('PYTHON'))
# endswith('!')  -> note: text has a trailing space, so check both raw and stripped
print("endswith('!'):", text.endswith('!'))
print("strip().endswith('!'):", text.strip().endswith('!'))


#===============PART-6===============
clean_text = text.strip().lower().replace(",", "").replace("!", "")
words = clean_text.split()
print("Clean text: ", clean_text)
print("Total characters: ", len(clean_text))
print("Total words: ", len(words))