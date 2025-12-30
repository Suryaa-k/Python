# • Create a custom context manager using @contextmanager from the contextlib
# module that opens a file, yields the file object, and ensures the file is closed
# even if an exception occurs.

from contextlib import contextmanager


@contextmanager
def safe_file_writer(filename):
    """Custom context manager using @contextmanager decorator"""
    print(f"🔓 Opening {filename} for writing...")
    file = None

    try:
        file = open(filename, 'w')
        yield file  # Yield file object to 'with' block

    finally:
        # Always executes, even if exception occurred
        if file:
            file.close()
            print(f"🔒 File {filename} closed successfully.")


# Demo usage
print("=== @contextmanager Demo ===\n")

# Test 1: Normal operation
print("Test 1: Normal writing")
with safe_file_writer('normal.txt') as f:
    f.write("Hello from @contextmanager!\n")
    f.write("File will be safely closed.\n")

print()

# Test 2: With exception
print("Test 2: Exception during writing")
try:
    with safe_file_writer('error.txt') as f:
        f.write("Writing before error...\n")
        x = 1 / 0  # ZeroDivisionError!
        f.write("This won't execute.\n")
except ZeroDivisionError:
    print("✅ Exception caught, but file still closed properly!")
