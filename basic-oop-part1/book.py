class Book:
    def __init__(self, title, price):
        self.__title = title
        self.__price = price

    @property
    def price(self):
        return self.__price

    @property
    def title(self):
        return self.__title

    def __str__(self):
        return f'{self.__title}, Price: {self.__price}'

pod_igoto = Book('Pod Igoto', 23.40)
print(pod_igoto.title)
print(pod_igoto.price)
print(pod_igoto)




