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

#this function is when a customer returns a book
    def return_book(self, book_name):
        print("Book Returned: Thank You \n")
        #this is to add book into the list of books because return
        self.books.append(book_name)

#this function is when a customer gives a book
    def donate_book(self, book_name):
        print("Book donated: Thank you for the donation \n")
        #this is to add book into list of books because donation
        #idk if dictionary is better instead of list maybe
        self.books.append(book_name)


#creating a new class for students 
class Student():
    def request_book(self):
        print("Do you want to borrow a book?")
        self.book = input("Enter the name of the book: ")
        return self.book
    
    def return_book(self):
        print("Do you want to return a book?")
        name = input("Enter your name: ")
        self.book = input("Enter the book your returning: ")
        #not sure if i did this right
        if {name: self.book} in track:
            track.remove({name: self.book})
        return self.book
    
    def donate_book(self):
        print("Do you want to donate a book?")
        self.book = input("Name of the book you want to donate: ")
        return self.book


if __name__ == "__main__":

    NJIT_library = Library(
        ["Computer Science", "Economy", "Biology", "Fiction", "Non-Fiction", "Math", "Finance"]
    )
    track = []

    print("\t\t\t Welcome to the NJIT library \n")
    print("Choose which option you want to do: -\n1 Listing all books \n2. Borrow Books \n3. Return books\n4. Donate books\n5. Track books\n6. exit the library\n")


    while(True):
        try:
            user_reponse = int(input("Enter your choice: "))
            
            if user_response == 1:
                
            
