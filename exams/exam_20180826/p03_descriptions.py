import re


class Person:
    def __init__(self, name: str, age: int, birthday: str):
        self.name = name
        self.age = age
        self.birthday = birthday

    def __str__(self):
        return f'Name of the person: {self.name}.\nAge of the person: {self.age}.\nBirthdate of the person: {self.birthday}.'


PATTERN = r'^.*name is [A-Z][a-z]+ [A-Z][a-z]+.* [1-9][0-9] years.*on [0-3][0-9]-[0-1][0-9]-[1-2][0-9]{3}.$'
NAME = r'name is [A-Z][a-z]+ [A-Z][a-z]+'
YEARS = r' [1-9][0-9] years'
BDAY = r'on [0-3][0-9]-[0-1][0-9]-[1-2][0-9]{3}.'

pattern = re.compile(PATTERN)
name_pattern = re.compile(NAME)
years_pattern = re.compile(YEARS)
bday_pattern = re.compile(BDAY)
persons_db = []
_input = input()

while not _input == "make migrations":
    if not pattern.search(_input):
        _input = input()
        continue
    else:
        name_info = name_pattern.search(_input).group().split()
        name = name_info[2] + ' ' + name_info[3]
        years_info = years_pattern.search(_input).group().rstrip().split()
        age = int(years_info[0])
        bday_info = bday_pattern.search(_input).group().split()
        birthday = bday_info[1].rstrip('.')
        person = Person(name, age, birthday)
        persons_db.append(person)
        _input = input()

if not len(persons_db):
    print('DB is empty')
else:
    for person in persons_db:
        print(person)
