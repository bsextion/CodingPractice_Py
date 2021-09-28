from enum import Enum
import string
from secrets import choice
import random
from abc import ABC, abstractmethod

class Genre(Enum):
    Romance = 1
    Fiction = 2
    NonFiction = 3
    History = 4
    Biography = 5


class BookSpec:
    def __init__(self, title,author, genre: Genre):
        self.title = title
        self.author = author
        self.genre = genre

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author

    def getGenre(self):
        return self.genre

class Book:
    def __init__(self, bookSpec: BookSpec):
        self.isbn = self.__id_generator()
        self.bookSpec = bookSpec
        self.isAvailable = True
        self.checked_out_by = None

    def __id_generator(size=6):
        return ''.join([choice(string.ascii_uppercase + string.digits) for _ in range(7)])


    def getIsbn(self):
        return self.isbn

    def getBookSpec(self):
        return self.bookSpec

    def getCheckedOutBy(self):
        return self.checked_out_by

    def setCheckedOutBy(self, id):
        self.checked_out_by = id

    def setAsAvailable(self):
        self.isAvailable = True

    def setAsUnAvailable(self):
        self.isAvailable = False

class Inventory:
    store = []

    def addBook(self, book:Book):
        exists = False
        if len(self.store) == 0:
            self.store.append(book)
            return

        for b in self.store:
            if b.getIsbn() == book.getIsbn():
                exists = True
                break

        if not exists:
            self.store.append(book)
        return

    def removeBook(self,id):
        found = filter(lambda x: x == id, self.store)
        self.store.remove(found)

    def checkBook(self, copies):
        # get the found books from search details
        #get the first book that is avialble else return None
        found = None
        for book in copies:
            if book.isAvailable:
                found = book
                break
        return found


    def search(self,book_details:BookSpec):
        found_books = []
        title = book_details.getTitle()
        author = book_details.getAuthor()
        genre = book_details.getGenre()

        found_books = list(filter(lambda b: b.getBookSpec().getTitle() == title  or b.getBookSpec().getAuthor() == author or b.getBookSpec().getGenre() == genre, self.store))
        return found_books

class User:

    def __init__(self, name, ):
        self.id = self.__id_generator()
        self.name = name

    def check_out(self, copies, inventory: Inventory):
        book = inventory.checkBook(copies)
        if book is None:
            print("Sorry there are no available copies to check out!")
        else:
            book.setCheckedOutBy(self.id)
            book.setAsUnAvailable()
            print("You have checked out a copy!")
        #get the first availble book returned by the search that is availiable and set it to checkout by user id

    def __id_generator(size=6, chars=string.digits):
        return ''.join(random.choice(chars) for _ in range(8))

def main():
    member_1 = User("cindy")
    member_2 = User("bob")

    harry_potter = BookSpec("Harry Potter Goblet of Fire", "JK Rowling", "Fiction")
    great_gatsby = BookSpec("The Great Gatsby", "F Scott", 'Fiction')

    book_1 = Book(harry_potter)
    book_2 = Book(great_gatsby)
    book_3 = Book(harry_potter)

    inventory = Inventory()
    inventory.addBook(book_1)
    inventory.addBook(book_2)
    inventory.addBook(book_3)

    searched_list = inventory.searchDetails(harry_potter)
    member_1.check_out(searched_list, inventory)

main()





