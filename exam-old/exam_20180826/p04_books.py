class Book:
    def __init__(self, title: str, author: str, price: float, chapters: list):
        self.title = title
        self.author = author
        self.price = price
        self.chapters = chapters

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if not len(value):
            raise Exception('Invalid book title')
        self.__title = value

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        if not len(value):
            raise Exception('Invalid book author')
        self.__author = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not value > 0:
            raise Exception('Invalid book price')
        self.__price = value

    @property
    def chapters(self):
        return self.__chapters

    @chapters.setter
    def chapters(self, value):
        if not len(value) > 0:
            raise Exception('Invalid book chapters')
        self.__chapters = value

    def __str__(self):
        return f'SOLD: {self.__title} with author {self.__author}. ' \
            f'Chapters in the book {len(self.chapters)}'


bookstore = []
books_sold = []

_input = input()

while not _input == 'on work':
    try:
        _input = _input.split(' -> ')
        title = _input[0].split()[0]
        author = _input[0].split()[1]
        price = float(_input[0].split()[2])
        chapters = _input[1].split(', ')
        book = Book(title, author, price, chapters)
        bookstore.append(book)
        _input = input()
    except:
        _input = input()
        continue

_input = input()
while not _input == "end work":
    books = [b for b in bookstore if b.title == _input]
    if not len(books):
        print('No such book here')
        _input = input()
        continue
    else:
        book = books[0]
        books_sold.append(book)
        _input = input()


if not len(books_sold):
    print('Bad day :(')
else:
    for book in books_sold:
        print(book)
    money = sum([b.price for b in books_sold])
    print(f'Money: {money:.2f}')
