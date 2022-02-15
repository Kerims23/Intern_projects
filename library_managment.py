from dbm.ndbm import library

#we are making a class to get books and initilze it compared to the last project
class library:
    def __init__(self, list_of_books):
        self.books = list_of_books

    def display_available_books(self):
        print(f"\n {len(self.books)} Availbale books: ")
        for book in self.books:
            print(f"---- {book}")
        print("\n")
