class Library:
    def __init__(self,listOfBooks):
        self.books=listOfBooks

    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books:
            print(" *"+book)

    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it whithin 30 days")
            self.books.remove(bookName)
        else:
            print("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available.")

    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")

class Student:
    def requestBook(self):
        self.book  = input("Enter the name of the book you want to borrow: ")
        return self.book
    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book 
            
if __name__=="__main__":
    centraLibrary = Library(["Algorithms","Django","Python Notes","Numpy","Data Structures"])
    s=Student()
    while(True):
        WelcomeMsg = '''\n======= Welcome to cental Library =======
        Please choose an option:
        1.List all the books
        2.Request a book
        3.Add/Return a book
        4.Exit the Library 
        '''
        print(WelcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centraLibrary.displayAvailableBooks()
        elif a == 2:
            centraLibrary.borrowBook(s.requestBook())
        elif a == 3:
            newbook=s.returnBook()
            if len(newbook)>0:
                centraLibrary.returnBook(newbook)
            else:
                print("Please enter a valid book name.")
        elif a == 4:
            print("Thanks for choosing central Library. Have a great day ahead!")
            exit()
        else:
            print("Invalid Choice!")