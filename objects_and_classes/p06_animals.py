from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def produce_sound(self):
        pass


class Dog(Animal):
    def __init__(self, name, age, number_of_legs):
        super().__init__(name, age)
        self.number_of_legs = number_of_legs

    def produce_sound(self):
        return f'I\'m a Distinguishedog, and I will now produce a distinguished sound! Bau Bau.'

    def print_info(self):
        return f'Dog: {self.name}, Age: {self.age}, Number Of Legs: {self.number_of_legs}'


class Cat(Animal):
    def __init__(self, name, age, intelligence_quotient):
        super().__init__(name, age)
        self.intelligence_quotient = intelligence_quotient

    def produce_sound(self):
        return f'I\'m an Aristocat, and I will now produce an aristocratic sound! Myau Myau.'

    def print_info(self):
        return f'Cat: {self.name}, Age: {self.age}, IQ: {self.intelligence_quotient}'


class Snake(Animal):
    def __init__(self, name, age, cruelty_coefficient):
        super().__init__(name, age)
        self.cruelty_coefficient = cruelty_coefficient

    def produce_sound(self):
        return f'I\'m a Sophistisnake, and I will now produce a sophisticated sound! Honey, I\'m home.'

    def print_info(self):
        return f'Snake: {self.name}, Age: {self.age}, Cruelty: {self.cruelty_coefficient}'


def produce_animal(_class, name, age, param):
    animal = None
    if _class == 'Dog':
        animal = Dog(name, age, param)
    elif _class == 'Cat':
        animal = Cat(name, age, param)
    else:
        animal = Snake(name, age, param)
    return animal


animals = []
_input = input()

while not _input == 'I\'m your Huckleberry':
    _input = _input.split()
    if len(_input) > 2:
        _class = _input[0]
        name = _input[1]
        age = _input[2]
        param = _input[3]
        animal = produce_animal(_class, name, age, param)
        animals.append(animal)
    else:
        animal = [a for a in animals if a.name == _input[1]][0]
        print(animal.produce_sound())
    _input = input()
dogs = [a for a in animals if isinstance(a, Dog)]
cats = [a for a in animals if isinstance(a, Cat)]
snakes = [a for a in animals if isinstance(a, Snake)]
sorted_animals = dogs + cats + snakes

for a in sorted_animals:
    print(a.print_info())
