class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}, Available: {self.is_available})"


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"Member: {self.name}, Borrowed Books: {', '.join([book.title for book in self.borrowed_books])}"


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.isbn] = book

    def remove_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]

    def add_member(self, member):
        self.members[member.name] = member

    def remove_member(self, name):
        if name in self.members:
            del self.members[name]

    def display_books(self):
        if not self.books:
            print("No books in the library")
        else:
            for book in self.books.values():
                print(book)

    def display_members(self):
        if not self.members:
            print("No members in the library")
        else:
            for member in self.members.values():
                print(member)

    def search_books(self, keyword):
        found_books = []

        for book in self.books.values():
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                found_books.append(book)

        if not found_books:
            print("No books found")
        else:
            for book in found_books:
                print(book)

    def borrow_book(self, member_name, isbn):
        if member_name in self.members and isbn in self.books:
            book = self.books[isbn]
            if book.is_available:
                member = self.members[member_name]
                member.borrowed_books.append(book)
                book.is_available = False
                print(f"{member_name} has borrowed '{book.title}'")
            else:
                print(f"'{book.title}' is not available")
        else:
            print("Member or book not found")

    def return_book(self, member_name, isbn):
        if member_name in self.members and isbn in self.books:
            member = self.members[member_name]
            book = next((b for b in member.borrowed_books if b.isbn == isbn), None)
            if book:
                member.borrowed_books.remove(book)
                book.is_available = True
                print(f"{member_name} has returned '{book.title}'")
            else:
                print(f"'{member_name}' did not borrow '{book.title}'")
        else:
            print("Member or book not found")

    def display_borrowed_books(self, member_name):
        if member_name in self.members:
            member = self.members[member_name]
            if not member.borrowed_books:
                print(f"{member_name} has not borrowed any books")
            else:
                print(f"{member_name}'s Borrowed Books:")
                for book in member.borrowed_books:
                    print(book)
        else:
            print("Member not found")


# Creating books
book1 = Book("Python Programming", "John Doe", "978-0134444321")
book2 = Book("Data Science Essentials", "Jane Smith", "978-1491981111")
book3 = Book("Web Development Basics", "Alice Johnson", "978-0987122101")

# Creating a library and adding books
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Displaying the library's books
print("Available Books:")
library.display_books()

# Creating members
member1 = Member("Alice")
member2 = Member("Bob")

# Adding members to the library
library.add_member(member1)
library.add_member(member2)

# Displaying the library's members
print("\nLibrary Members:")
library.display_members()

# Simulating book borrowing and returning
library.borrow_book("Alice", "978-0134444321")
library.borrow_book("Bob", "978-0134444321")
library.borrow_book("Bob", "978-1491981111")
library.return_book("Bob", "978-1491981111")

# Displaying the library's books after borrowing and returning
print("\nAvailable Books after transactions:")
library.display_books()

# Displaying the library's members after transactions
print("\nLibrary Members after transactions:")
library.display_members()

# Searching for books
print("\nSearching for books with 'Python' in the title or author:")
library.search_books("Python")

# Displaying borrowed books for a member
print("\nDisplaying borrowed books for Alice:")
library.display_borrowed_books("Alice")
