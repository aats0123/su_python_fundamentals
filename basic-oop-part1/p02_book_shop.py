class Book:
    def __init__(self, title: str, author: str, price: float):
        self.title = title
        self.author = author
        self.price = price
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if len(value) < 3:
            print('Title not valid!')
            exit(0)
        else:
            self.__title = value

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        if len(value.split()) > 1 and value.split()[1][0].isdigit():
            print('Author not valid!')
            exit(0)
        else:
            self.__author = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0.0:
            print('Price not valid!')
            exit(0)
        else:
            self.__price = value

    def __str__(self):
        return f"Type: {self.__class__.__name__}\nTitle: {self.title}\nAuthor: {self.author}\nPrice: {self.price:.2f}"

class GoldenEditionBook(Book):

    @property
    def price(self):
        return self.__price

    @Book.price.setter
    def price(self, value):
        Book.price.fset(self, value * 1.3)

author = input()
title = input()
price = float(input())

book = Book(title, author, price)
golden_edition_book = GoldenEditionBook(title, author, price)
print(book)
print()
print(golden_edition_book)