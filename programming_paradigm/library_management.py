# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title                 # public attribute
        self.author = author               # public attribute
        self._is_checked_out = False       # private attribute

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as available again."""
        self._is_checked_out = False

    def is_available(self):
        """Return True if book is not checked out."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []   # private list storing Book objects

    def add_book(self, book):
        """Add a new Book object to the library."""
        self._books.append(book)
        

    def check_out_book(self, title):
        """Check out a book by title if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False

    def return_book(self, title):
        """Return a checked-out book."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return True
        return False

    def list_available_books(self):
        """Print all books that are available."""
        available = [
            f"{book.title} by {book.author}"
            for book in self._books
            if book.is_available()
        ]

        for entry in available:
            print(entry)

