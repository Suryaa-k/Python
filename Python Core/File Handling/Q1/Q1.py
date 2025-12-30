# • Write a Python program using a context manager (with) to open a text file in
# read mode, read the entire content using read(), and print the number of
# characters in the file.

with open('sample.txt', 'w') as f:
    f.write("Hello World!\nThis is a test file.\nPython file handling.")

filename = 'sample.txt'

try:
    with open(filename, 'r') as file:  # Context manager
        content = file.read()          # Read entire content
        char_count = len(content)
        print(f"File '{filename}' has {char_count} characters.")
        print(f"Content preview: {content[:50]}...")
except FileNotFoundError:
    print(f"Error: '{filename}' not found!")
except PermissionError:
    print("Error: Permission denied!")
