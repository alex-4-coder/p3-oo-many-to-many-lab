class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    # name getter/setter
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise Exception("Name must be a non-empty string.")

    # Relationships
    def contracts(self):
        """Return all contracts belonging to this author."""
        return [contract for contract in Contract.all if contract.author is self]

    def books(self):
        """Return all books this author has contracts for."""
        return [contract.book for contract in self.contracts()]

    # Actions
    def sign_contract(self, book, date, royalties):
        """Create a new contract and return it."""
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """Return sum of royalties across all contracts."""
        return sum(contract.royalties for contract in self.contracts())

    def __repr__(self):
        return f"<Author {self.name}>"


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    # title getter/setter
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._title = value
        else:
            raise Exception("Title must be a non-empty string.")

    def contracts(self):
        """Return all contracts for this book."""
        return [contract for contract in Contract.all if contract.book is self]

    def authors(self):
        """Return all authors for this book via contracts."""
        return [contract.author for contract in self.contracts()]

    def __repr__(self):
        return f"<Book {self.title}>"


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    # author property
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value
        else:
            raise Exception("Author must be an instance of Author class.")

    # book property
    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if isinstance(value, Book):
            self._book = value
        else:
            raise Exception("Book must be an instance of Book class.")

    # date property
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._date = value
        else:
            raise Exception("Date must be a non-empty string.")

    # royalties property
    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if isinstance(value, int) and value >= 0:
            self._royalties = value
        else:
            raise Exception("Royalties must be a non-negative integer.")

    # Class method
    @classmethod
    def contracts_by_date(cls, date):
        """Return all contracts with the given date."""
        return [contract for contract in cls.all if contract.date == date]

    def __repr__(self):
        return f"<Contract {self.author.name} - {self.book.title} ({self.date})>"
