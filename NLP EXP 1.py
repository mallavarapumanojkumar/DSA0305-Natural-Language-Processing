import re

text = input("Enter the text: ")
pattern = input("Enter the pattern to search: ")

match = re.search(pattern, text)

if match:
    print("Pattern found!")
    print("Matched text:", match.group())
    print("Position:", match.start())
else:
    print("Pattern not found.")
