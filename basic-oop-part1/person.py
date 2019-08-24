from abc import ABC, abstractmethod


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 3:
            print("Name's length should not be less than 3 symbols!")
            exit(0)
        else:
            self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            print("Age must be positive!")
            exit(0)
        else:
            self.__age = value

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

#    def __eq__(self, other):
#       return (self.__name == other.__name) and (self.__age == other.__age)


class Child(Person):

    @property
    def age(self):
        return self.__age

    @Person.age.setter
    def age(self, value):
        if value > 15:
            print("Child's age must be less than 15!")
            exit(0)
        else:
            Person.age.fset(self, value)


age = int(input())
name = input()

child = Child(name, age)
print(child)
