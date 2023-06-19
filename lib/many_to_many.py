class Author:
    def __init__(self, name):
        self.name = name
        self.contracts_list = []
    
    def __repr__(self):
        return f"Author(name='{self.name}')"
        
    def contracts(self):
        return self.contracts_list
    
    def books(self):
        book_set = set()  # Create a set to store unique books
        
        for contract in self.contracts_list:
            book = contract.book
            if book:
                book_set.add(book)
        
        return list(book_set)
    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self.contracts_list.append(contract)
        return contract
    def total_royalties(self):
        total = 0
        for c in self.contracts_list:
            total += c.royalties
        return total

class Book:
    def __init__(self, title):
        self.title = title
        self.contracts_list = []
        self.authors_list = []
    def __repr__(self):
        return f"Title(name='{self.title}')"
    def contracts(self):
        return self.contracts_list
    def authors(self):
        return self.authors_list

class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        book.authors_list.append(author)
        self.all.append(self)
    def __repr__(self):
        return f"Contract(author={self.author.name}, book={self.book.title}, date={self.date}, royalties={self.royalties})"
    def contracts_by_date():
        return sorted(Contract.all, key=lambda c: c.date)
    def get_author(self):
        return self._author
    def set_author(self, author):
        if isinstance(author, Author):
            author.contracts_list.append(self)
            self._author = author
        else:
            raise Exception('please enter an author')
    author = property(get_author, set_author)
    def get_book(self):
        return self._book
    def set_book(self, book):
        if isinstance(book, Book):
            self._book = book
            book.contracts_list.append(self)
        else:
            raise Exception('please enter a book')
    book = property(get_book, set_book)
    def get_date(self):
        return self._date
    def set_date(self, date):
        if type(date) == str:
            self._date = date
        else:
            raise Exception('please enter a date')
    date = property(get_date, set_date)
    def get_royalties(self):
        return self._royalties
    def set_royalties(self, royalties):
        if type(royalties) == int:
            self._royalties = royalties
        else:
            raise Exception('please enter a number')
    royalties = property(get_royalties, set_royalties)