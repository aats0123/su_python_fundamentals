from abc import ABC, abstractmethod


class Item(ABC):
    @abstractmethod
    def __init__(self, id: str, operating_system: str, price: float):
        self.id = id
        self.operating_system = operating_system
        self.price = price

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if not len(value) > 7 or not value.isalpha():
            raise Exception("Invalid id!")
        else:
            self.__id = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise Exception("Invalid price!")
        else:
            self.__price = value

    def __str__(self):
        return f'Item id: {self.id}\nOperating system: {self.operating_system}\nPrice: {self.price}'


class Phone(Item):
    @abstractmethod
    def __init__(self, id, operating_system, price):
        Item.__init__(self, id, operating_system, price)

    def make_call(self):
        return "Making call..."

    def receive_call(self):
        return "Receiving a call!"

    def send_message(self):
        return "Sending message..."

    def receive_message(self):
        return "Receiving a message!"


class SmartPhone(Phone):

    def __init__(self, id, operating_system, price, applications):
        Phone.__init__(self, id, operating_system, price)
        self.applications = applications

    @property
    def applications(self):
        return self.__applications

    @applications.setter
    def applications(self, value):
        if len(value) < 5:
            raise Exception("Invalid number of applications!")
        else:
            self.__applications = value

    def browse_internet(self):
        return "Browsing..."

    def __str__(self):
        apps = ' '.join(self.applications)
        return Phone.__str__(self) + f'\nApplications: ' + ', '.join(self.applications)


class CellPhone(Phone):
    def __init__(self, id, operating_system, price):
        Phone.__init__(self, id, operating_system, price)


class Tablet(Item):
    def __init__(self, id, operating_system, price):
        Item.__init__(self, id, operating_system, price)

    def stream_movie(self):
        return "Streaming movie..."


items_list = []
output = ''
data = input()
while not data == 'end':
    try:
        item = eval(data)
        items_list.append(item)
    except Exception as ex:
        output += f'\n{ex}'
    data = input()

data = input()
while not data == 'end':
    command = data.split()[0]
    if command == 'test':
        id = data.split()[1]
        functionality = data.split()[2]

        try:
            item = [i for i in items_list if i.id == id][0]
            curr_func = getattr(item, functionality)
            output += '\n' + curr_func()
        except:
            output += "\nInvalid request has been made!"
    elif command == 'report':
        kind = data.split()[1]
        items = [i for i in items_list if i.__class__.__name__ == kind]
        if len(items) == 0:
            output += '\nInvalid request has been made!'
        else:
            for item in items:
                output += '\n' + item.__str__()

    data = input()
output = output.rstrip('\n')
print(output)
