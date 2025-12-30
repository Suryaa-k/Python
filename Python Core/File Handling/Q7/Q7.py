# • Write a program using a context manager that opens a file in read mode, uses a
# loop to read the file in small chunks (for example, 5 characters at a time),
# prints the cursor position after each read using tell(), uses seek() to move to
# a specific position, and continues reading from there.

filename = 'chunk_demo.txt'

# Create sample file first (long enough for demo)
with open(filename, 'w') as f:
    f.write("Python file handling with context managers is powerful and safe.\n")
    f.write("This demonstrates chunked reading and cursor control precisely.")

print("=== Chunked File Reading with Cursor Control ===\n")

try:
    with open(filename, 'r') as file:
        chunk_size = 5
        total_read = 0

        print(f"Reading in chunks of {chunk_size} characters...")
        print("-" * 60)

        # Step 1: Read first few chunks
        for i in range(3):  # Read first 15 chars (3 chunks)
            chunk = file.read(chunk_size)
            if chunk:
                position = file.tell()
                print(f"Chunk {i + 1}: '{chunk}' | Position: {position}")
                total_read += len(chunk)
            else:
                print("End of file reached")
                break

        # Step 2: Jump to position 20
        target_pos = 20
        file.seek(target_pos)
        print(f"\n🔄 Jumped to position {target_pos}")
        print(f"Current position: {file.tell()}")

        # Step 3: Continue reading from new position
        print("Continuing from position 20:")
        print("-" * 40)
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            position = file.tell()
            print(f"Chunk: '{chunk}' | Position: {position}")

        print(f"\n📊 Summary: Total chars read in first phase: {total_read}")

except FileNotFoundError:
    print(f"Error: '{filename}' not found!")
except PermissionError:
    print("Error: Permission denied!")
