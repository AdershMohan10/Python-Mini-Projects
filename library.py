class Book:
    def __init__(self, title, author, isbn, available_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.__available_copies = available_copies

    def get_available_copies(self):
        return self.__available_copies

    def set_available_copies(self, count):
        if count >= 0:
            self.__available_copies = count

    def display_details(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available Copies: {self.__available_copies}")


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def max_books_allowed(self):
        return 2

    def borrow_book(self, library, title):
        try:
            book = library.find_book_by_title(title)
            if book:
                if book.get_available_copies() > 0:
                    if len(self.borrowed_books) < self.max_books_allowed():
                        self.borrowed_books.append(book.title)
                        book.set_available_copies(book.get_available_copies() - 1)
                        print(f"{self.name} borrowed '{book.title}'.")
                    else:
                        print(f"{self.name} has reached the borrowing limit.")
                else:
                    print("Book not available.")
            else:
                raise ValueError("Book not found in the library.")
        except ValueError as e:
            print(f"Error: {e}")

    def return_book(self, library, title):
        try:
            if title in self.borrowed_books:
                book = library.find_book_by_title(title)
                if book:
                    self.borrowed_books.remove(title)
                    book.set_available_copies(book.get_available_copies() + 1)
                    print(f"{self.name} returned '{book.title}'.")
                else:
                    raise ValueError("Book not found in the library.")
            else:
                raise ValueError(f"{self.name} never borrowed '{title}'.")
        except ValueError as e:
            print(f"Error: {e}")

    def display_details(self):
        print(f"Member: {self.name}, ID: {self.member_id}, Borrowed: {self.borrowed_books}")


class PremiumMember(Member):
    def max_books_allowed(self):
        return 5


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, isbn):
        self.books = [b for b in self.books if b.isbn != isbn]

    def register_member(self, member):
        self.members.append(member)

    def remove_member(self, member_id):
        self.members = [m for m in self.members if m.member_id != member_id]

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def find_books_by_author(self, author):
        return [b for b in self.books if b.author.lower() == author.lower()]

    def display_all_books(self):
        print("\n---- Library Books ----")
        for book in self.books:
            book.display_details()

    def display_all_members(self):
        print("\n---- Library Members ----")
        for member in self.members:
            member.display_details()


if __name__ == "__main__":
    library = Library()

    b1 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "ISBN001", 3)
    b2 = Book("Game of Thrones", "George R.R. Martin", "ISBN002", 1)
    b3 = Book("Percy Jackson and the Lightning Thief", "Rick Riordan", "ISBN003", 0)
    library.add_book(b1)
    library.add_book(b2)
    library.add_book(b3)

    m1 = Member("Adersh", "M101")
    m2 = PremiumMember("Arjun", "M102")
    library.register_member(m1)
    library.register_member(m2)

    library.display_all_books()
    library.display_all_members()

    print("\n---- Borrowing Books ----")
    m1.borrow_book(library, "Harry Potter and the Sorcerer's Stone")
    m1.borrow_book(library, "Percy Jackson and the Lightning Thief")
    m2.borrow_book(library, "Game of Thrones")
    m2.borrow_book(library, "The Hobbit")

    print("\n---- Returning Books ----")
    m1.return_book(library, "Harry Potter and the Sorcerer's Stone")
    m1.return_book(library, "The Alchemist")

    print("\n---- Final Library Status ----")
    library.display_all_books()
