# • Create a custom context manager using a class that opens a file in write mode
# in the __enter__ method, writes a line to the file, closes the file in the
# __exit__ method, and properly prints or logs any exception information received
# in __exit__.

class SafeFileWriter:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        """Open file in write mode"""
        print(f"Opening {self.filename} for writing...")
        self.file = open(self.filename, 'w')
        return self.file  # Return file object for 'with file as f:'

    def __exit__(self, exc_type, exc_value, traceback):
        """Close file and handle exceptions"""
        if self.file:
            self.file.close()
            print(f"File {self.filename} closed successfully.")

        # Log exception info if any occurred
        if exc_type is not None:
            print(f"❌ EXCEPTION occurred:")
            print(f"  Type: {exc_type.__name__}")
            print(f"  Value: {exc_value}")
            print(f"  Traceback: {traceback}")
            return False  # Don't suppress exception
        return True  # No exception, suppress nothing


# Demo usage
print("=== Custom Context Manager Demo ===\n")

# Test 1: Normal operation
print("Test 1: Normal writing")
with SafeFileWriter('output.txt') as f:
    f.write("Hello from custom context manager!\n")
    f.write("This demonstrates __enter__ and __exit__.")

print()

# Test 2: With exception
print("Test 2: Writing with deliberate error")
try:
    with SafeFileWriter('error_log.txt') as f:
        f.write("This will cause an error...\n")
        x = 1 / 0  # ZeroDivisionError!
        f.write("This won't execute.")
except Exception:
    pass  # Context manager already handled it
