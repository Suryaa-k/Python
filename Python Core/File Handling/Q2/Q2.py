# • Write a program that opens a file using a context manager, reads all lines
# using readlines(), and prints only the lines that contain more than 10
# characters.

with open('lines.txt', 'w') as f:
    f.write("Short\n")
    f.write("This line has more than ten characters\n")
    f.write("Medium\n")
    f.write("Another very long line with lots of characters here\n")
    f.write("Short again\n")

filename = 'lines.txt'

try:
    with open(filename, 'r') as file:
        lines = file.readlines()  # Returns list of lines with \n

        print(f"Total lines: {len(lines)}")
        print("Lines > 10 characters:")
        print("-" * 30)

        for i, line in enumerate(lines, 1):
            if len(line.strip()) > 10:  # strip() removes \n for accurate count
                print(f"Line {i}: {repr(line.rstrip())} ({len(line.strip())} chars)")

except FileNotFoundError:
    print(f"Error: '{filename}' not found!")
except PermissionError:
    print("Error: Permission denied!")
