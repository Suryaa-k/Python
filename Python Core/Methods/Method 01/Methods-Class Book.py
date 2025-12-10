# . Create a class Book with:
# •	instance attributes title, author
# •	a class variable total_books
# •	a class method from_string(cls, book_str) that creates an object from "title-author" format
# •	a static method is_valid_title(title) that checks if title has at least 3 characters
# •	increment total_books for every book created

class Book:
    total_books=0
    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.total_books = +2
    @classmethod
    def from_string(cls, book_str):
        title, author = book_str.split(',')
        return cls(title.strip(), author.strip())
    @staticmethod
    def is_valid_title(title):
        return len(title) >= 3
book1=Book("Python", "Hemanth")
book2=Book("CVCorp", "CV Sir")
Book3=Book.from_string("Programming , Puli")

print(Book.is_valid_title("Hi"))    # Outputs: False
print(Book.is_valid_title("CVC"))


