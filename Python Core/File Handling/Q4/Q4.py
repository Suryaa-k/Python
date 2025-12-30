# • Write a program that opens a file in read mode, reads the first 10 characters,
# prints the current cursor position using tell(), moves the cursor back to the
# beginning using seek(0), and reads the full content again.

filename = 'cursor_demo.txt'

# Create sample file first
with open(filename, 'w') as f:
    f.write("Python file handling is easy to learn.\n")
    f.write("This demonstrates cursor position control.\n")
    f.write("seek() and tell() work together perfectly.")

print("=== File Cursor Demo ===\n")

try:
    with open(filename, 'r') as file:
        # Step 1: Read first 10 characters
        first_10 = file.read(10)
        print(f"1. First 10 chars: '{first_10}'")

        # Step 2: Print current cursor position
        position = file.tell()
        print(f"2. Cursor position after 10 chars: {position}")

        # Step 3: Move cursor back to beginning
        file.seek(0)
        print("3. Cursor moved back to position 0")

        # Step 4: Verify position and read full content
        new_position = file.tell()
        print(f"4. New cursor position: {new_position}")

        full_content = file.read()
        print(f"\n5. Full content ({len(full_content)} chars):")
        print("-" * 50)
        print(repr(full_content))  # Shows exact content with \n

except FileNotFoundError:
    print(f"Error: '{filename}' not found!")
