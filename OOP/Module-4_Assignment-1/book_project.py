class Library:
    book_list = []

    @classmethod
    def entry_book(self,books):
        self.book_list.append(books)

    @classmethod
    def view_all_books(self):
        if len(self.book_list) == 0:
            print('No books available in the library')
        else:
            for book in self.book_list:
                book.view_book_info()
    
    @classmethod
    def find_book(self,book_id):
        for book in self.book_list:
            if book.get_book_id() == book_id:
                return book
        return None
    

class Book:
    def __init__(self,book_id,title,author,availability):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = availability
        Library.entry_book(self)

    def get_book_id(self):
        return self.__book_id

    def borrow_book(self):
        if self.__availability == True:
            self.__availability = False
            print(f'\nYou borrowed: {self.__title}')
        else:
            print(f'\nSorry, the book is not available')

    def return_book(self):
        if self.__availability == False:
            self.__availability = True
            print(f'You returned: {self.__title}')
        else:
            print(f'{self.__title} book is already available in the library')

    def view_book_info(self):
        print(f'ID: {self.__book_id}, Title: {self.__title}, Author: {self.__author},',end=' ')
        if self.__availability == True:
            print('Availability: Available')
        else:
            print('Availability: Not Available')            

    
book1 = Book(101,'Marhaba JS e maro thaba','Jhankar Mahbub',True)
book2 = Book(102,'English Therapy','Saiful Islam',False)
book2 = Book(103,'Spoken English','Munjerin Shahid',True)

# book2.view_book_info()

def menu_options():
    while True:
        print('\n-------Menu-------')
        print('1. View All Books\n2. Borrow Books\n3 .Return Book\n4. Exit')
        
        n = int(input('\nEnter your choice: '))
        if n < 1 or n > 4:
            print('\nInvalid choice. Please enter a number from 1 to 4')
            continue

        if n == 1:
            Library.view_all_books()
        elif n == 2:
            id = int(input('\nEnter the book ID to borrow: '))
            book  = Library.find_book(id)
            if book:
                book.borrow_book()
            else:
                print('\nInvalid book ID')
        elif n == 3:
            id = int(input('\nEnter the book ID to return: '))
            book = Library.find_book(id)
            if book:
                book.return_book()
            else:
                print('\nInvalid book ID')
        else:
            print('\nExiting the library system')
            break


menu_options()