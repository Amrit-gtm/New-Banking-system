class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, quantity):
        if title in self.books:
            self.books[title] += quantity
        else:
            self.books[title] = quantity

    def borrow_book(self, title):
        if title in self.books and self.books[title] > 0:
            self.books[title] -= 1
            print(f"Borrowed {title}.")
        else:
            print(f"{title} is not available.")

    def return_book(self, title):
        if title in self.books:
            self.books[title] += 1
        else:
            self.books[title] = 1

    def get_inventory(self):
        return self.books

    def get_available_books(self):
        return [title for title, quantity in self.books.items() if quantity > 0]

# Test cases
library = Library()

library.add_book("The Great Gatsby", 3)
library.add_book("1984", 2)
library.add_book("To Kill a Mockingbird", 1)

library.borrow_book("1984")
print(library.get_inventory())  # Expected output: {'The Great Gatsby': 3, '1984': 1, 'To Kill a Mockingbird': 1}


library.borrow_book("The Great Gatsby")  # Expected output: The Great Gatsby is not available.

library.return_book("1984")
print(library.get_inventory())  # Expected output: {'The Great Gatsby': 0, '1984': 2, 'To Kill a Mockingbird': 1}

print(library.get_available_books())  # Expected output: ['1984', 'To Kill a Mockingbird']

