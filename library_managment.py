#we are making a class to get books and initilze it compared to the last project
class Library:
    def __init__(self, list_of_books):
        self.books = list_of_books

#this is to display all the books in the library
    def display_available_books(self):
        print(f"\n {len(self.books)} Availbale books: ")
        for book in self.books:
            print(f"---- {book}")
        print("\n")

    def borrow_book(self, name, book_name):
        if book_name not in self.books:
            print(f"{book_name} is not available, wait for return")
        else:
            