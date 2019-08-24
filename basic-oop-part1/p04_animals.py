from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value <= 0:
            raise Exception('Invalid input!')
        else:
            self.__age = value

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        self.__gender = value

    def __str__(self):
        return f"{self.__class__.__name__}\n{self.name} {self.age} {self.gender}\n" + self.produce_soud()

    @abstractmethod
    def produce_soud(self):
        pass


class Dog(Animal):
    def produce_soud(self):
        return "Woof!"


class Frog(Animal):
    def produce_soud(self):
        return "Ribbit"


class Cat(Animal):
    def produce_soud(self):
        return "Meow meow"


class Kitten(Cat):
    def __init__(self, name, age, gender = 'Female'):
        super().__init__(name, age, gender)

    def produce_soud(self):
        return "Meow"


class Tomcat(Cat):
    def __init__(self, name, age, gender = 'Male'):
        super().__init__(name, age, gender)

    def produce_soud(self):
        return "MEOW"

def create_dog(animal_info):
    try:
        dog = Dog(animal_info[0], int(animal_info[1]), animal_info[2])
        return dog
    except:
        return 'Invalid input!'

def create_frog(animal_info):
    try:
        frog = Frog(animal_info[0], int(animal_info[1]), animal_info[2])
        return frog
    except:
        return'Invalid input!'

def create_cat(animal_info):
    try:
        cat = Cat(animal_info[0], int(animal_info[1]), animal_info[2])
        return cat
    except:
        return 'Invalid input!'

def create_kitten(animal_info):
    try:
        kitten = Kitten(animal_info[0], int(animal_info[1]))
        return kitten
    except:
        return 'Invalid input!'

def create_tomcat(animal_info):
    try:
        tomcat = Tomcat(animal_info[0], int(animal_info[1]))
        return tomcat
    except:
        return 'Invalid input!'

animal_factory = {
    'Dog':create_dog,
    'Cat':create_cat,
    'Frog':create_frog,
    'Kitten':create_kitten,
    'Tomcat':create_tomcat
}
animals_list = []
_input = input()

while not _input == 'Beast!':
    animal_type = _input
    animal_info = input().split()

    if animal_type not in ['Dog', 'Cat', 'Frog', 'Kitten', 'Tomcat'] or len(animal_info) < 3:
        print('Invalid input!')
        _input = input()
        continue
    else:
        animal = animal_factory[animal_type](animal_info)
        animals_list.append(animal)

    _input = input()

for animal in animals_list:
    print(animal)



