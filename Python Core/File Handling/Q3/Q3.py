# • Write a program that creates a file and writes 3 lines using write(), reopens
# the same file in append mode, appends 2 more lines, and finally reads and prints
# the complete file content.

filename = 'combined.txt'

# Step 1: Create file and write 3 lines
print("Step 1: Writing 3 lines...")
with open(filename, 'w') as file:
    file.write("Line 1: First written line\n")
    file.write("Line 2: Second written line\n")
    file.write("Line 3: Third written line\n")

# Step 2: Reopen in append mode and add 2 more lines
print("Step 2: Appending 2 lines...")
with open(filename, 'a') as file:
    file.write("Line 4: First appended line\n")
    file.write("Line 5: Second appended line\n")

# Step 3: Read and print complete content
print("Step 3: Reading complete file...")
try:
    with open(filename, 'r') as file:
        content = file.read()
        print("\nComplete file content:")
        print("-" * 40)
        print(content)
        print(f"\nTotal characters: {len(content)}")

except FileNotFoundError:
    print(f"Error: '{filename}' not found!")
