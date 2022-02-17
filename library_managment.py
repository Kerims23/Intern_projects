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
            print(f"{book_name} is not available, wait for return \n")
        else:
#made a list here to track the books, is dictionary better here?
            track.append({name: book_name})
            print("Successful, return the book on time in good condition \n")
            #this should remove the book being borrowed 
            self.books.remove(book_name)

    def return_book(self, book_name):
        print("Book Returned: Thank You \n")
        self.books.append(book_name)

    def donate_book(self, book_name):
        print("Book donated: Thank you for the donation \n")







track = []