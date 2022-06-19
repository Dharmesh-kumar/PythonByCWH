# #create a library
# # then define methods:
# # display book
# # lend book  - who owns the if not present in library
# # add book
# # return book
#
# class Library:
#
#      def __init__(self,list_of_books,Library_name):
#          self.lend_data = {}
#          self.list_of_books= list_of_books
#          self.library_name= Library_name
#
#         #adding books to dictionary
#          for books in self.list_of_books:
#            #none means no reader have lend this book
#             self.lend_data=None
#
#      def display_books(self):
#            for index, books in enumerate(self.list_of_books):
#                print(f"{index}:{books}")
#
#      def lend_book(self, book , reader):
#          if book in self.list_of_books:
#              if self.lend_data[book] is None:
#                  self.lend_data[book]= reader
#                  print("book lend")
#              else:
#                  print(f"Sorry This book is lend by {self.lend_data[book]}")
#          else:
#              print("You have written the wrong book name")
#
#      def return_book(self, book, reader):
#          if book in self.list_of_books:
#              if self.lend_data[book] is not None:
#                  self.lend_data.pop(book)
#              else :
#                  print("Sorry but this book is not lend")
#          else:
#              print("sorry you have written wrong book name")
#      def add_book(self, book_name):
#          self.list_of_books.append(book_name)
#          self.lend_data[book_name] = None
#
#      def delete_book(self, book_name):
#          self.list_of_books.remove(book_name)
#          self.lend_data.pop(book_name)
#
#
#
# def main():
#     #by default varibles
#     list_books = {"cookbook","sherlock holmes","Lucifer","breaking bed","Rich dad poor dad"}
#     Library_name = "Manu"
#     secret_key = 12345
#
#     Manu = Library(list_books , Library_name)
#
#     print(f"Welcome to {Manu.library_name} library\n\npress 'q' for Exit \nDisplay book using 'd'\nAdd lend book using 'l' and return a book using 'r' \nAdd a book using 'a' \ndelete book using 'del'\n" )
#
#     Exit = False
#     while(Exit is not True):
#         _input = input("Option: ")
#         if _input == "q":
#             Exit = True
#         elif _input == "d":
#             Manu.display_books()
#         elif _input == "l":
#           _input2 = input("What is your name:")
#           _input3 = input("Which book do you want to lend: ")
#
#           Manu.lend_book(_input2,_input3)
#
#         elif _input == "a":
#             _input2 = input("book name")
#             Manu.add_book(_input2)
#
#         elif _input == "del":
#             _input_secret = input("...Write the code of the secret key sp that you will be able to delete...")
#             if _input_secret == secret_key:
#                _input2 = print(input("which book do you want to delete"))
#                Manu.delete_book(_input2)
#
#             else:
#                 print("Sorry er can't delete the book")
#
#         elif _input == "r":
#             _input2 = input("What is your name: ")
#             _input3 = input("Which book do you want to return: ")
#             Manu.return_book(_input3 , _input2)
#
# if __name__ == "__main__":
#     main()
import time
class library:
    def __init__(self,list,name):
        self.booksList = list
        self.name =name
        self.lendDict ={}

    def displayBooks(self):
        print(f"We have following books in the library {self.name}")
        for book in self.booksList:
            print(book)
    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("lender-book database has ben updated you can take the book now")
        else:
            print(f"book is already being used by {self.lendDict[user]}")

    def addBook(self,book):
        self.booksList.append(book)
        print(f"book has been added to the book list")


    def returnBook(self,book):
        self.lendDict.pop(book)


if __name__ == '__main__':
    manu= library(["python","rick dad poor dad","c++ basics","Harry potter","Algorithm by CLRS"],"PORTAL")
    while(True):
        print(f"Welcome to the {manu.name} library. Enter you choice to continue")
        print("1. Display books")
        print("2. lend a books")
        print("3. Add a books")
        print("4. Return a books")
        user_choice = (input())
        if user_choice not in ['1','2','3','4']:
            print("please enter a valid option")
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            manu.displayBooks()

        elif user_choice == 2:
            book= input("Enter the name of the book you want to lend: ")
            user=input("Enter you name: ")
            manu.lendBook(user,book)

        elif user_choice == 3:
            book=input("Enter the name of the book you want to add: ")
            manu.addBook(book)

        elif user_choice == 4:
            book=input("Enter the book you want to return: ")
            manu.returnBook(book)
            time.sleep(2)
            print("the book is returned")

        print("press q to quit and c to continue")
        user_choice2 = input()

        if user_choice2 == "q":
             exit()
        elif user_choice2 == "c":
           continue
        else:
           print("Please enter a valid option")