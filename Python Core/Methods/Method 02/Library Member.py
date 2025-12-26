# Q9. Design a LibraryMember class that:
# •	Tracks total active members.
# •	Each member has a name and books_borrowed count.
# •	Has a function to borrow books, with borrowing limit common to all.
# •	Allows updating borrowing limit globally.
# •	Has a static function to check if book title is valid (non-empty string, reasonable length).

class LibraryMember:
    total_active_members = 0
    borrowing_limit = 3

    def __init__(self, name):
        self.name = name
        self.books_borrowed = 0
        LibraryMember.total_active_members += 1

    @staticmethod
    def is_valid_book_title(title):
        title_str = str(title)
        if title_str == "" or title_str is None:
            return False
        length = 0
        for char in title_str:
            length += 1
            if length > 50:
                return False
        return length > 0

    def borrow_book(self):
        if self.books_borrowed < LibraryMember.borrowing_limit:
            self.books_borrowed += 1
            return True
        return False

    def return_book(self):
        if self.books_borrowed > 0:
            self.books_borrowed -= 1
            return True
        return False

    @classmethod
    def update_borrowing_limit(cls, new_limit):
        if new_limit >= 0:
            cls.borrowing_limit = new_limit

member1 = LibraryMember("Rahul")
member2 = LibraryMember("Priya")
member3 = LibraryMember("Amit")

print("Total active members:", LibraryMember.total_active_members)

member1.borrow_book()
member1.borrow_book()
member2.borrow_book()

print(f"{member1.name}: {member1.books_borrowed} books")
print(f"{member2.name}: {member2.books_borrowed} books")

print("Can Rahul borrow more?", member1.borrow_book())
print(f"{member1.name}: {member1.books_borrowed} books")

print("\nBook title checks:")
print("Harry Potter:", LibraryMember.is_valid_book_title("Harry Potter"))
print("A:", LibraryMember.is_valid_book_title("A"))
print("Empty:", LibraryMember.is_valid_book_title(""))
print("Long title:", LibraryMember.is_valid_book_title("VeryLongBookTitleOver50CharactersHere"))

LibraryMember.update_borrowing_limit(5)
print("New borrowing limit:", LibraryMember.borrowing_limit)
print("Can Rahul borrow more?", member1.borrow_book())

