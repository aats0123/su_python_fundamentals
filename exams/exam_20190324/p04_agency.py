from abc import ABC, abstractmethod


class Apartment(ABC):

    def __init__(self, id: str, rooms: int, baths: int, square_meters: float, price: float):
        self.id = id
        self.rooms = rooms
        self.baths = baths
        self.square_meters = square_meters
        self.price = price
        self.occupied = False

    @abstractmethod
    def __str__(self):
        return f'{self.rooms} rooms place with {self.baths} bathroom/s.' \
            f'\n{float(self.square_meters)} sq. meters for {float(self.price)} lv.'


class LivingApartment(Apartment):

    def __str__(self):
        return Apartment.__str__(self)


class OfficeApartment(Apartment):

    def __str__(self):
        return Apartment.__str__(self)


apartments = []
output = ''
_input = input()
while not _input == 'start_selling':
    try:
        apartment = eval(_input)
        apartments.append(apartment)
    except Exception as ex:
        output += f'\n{ex}'
    _input = input()

_input = input()
while not (_input == 'taken' or _input == 'free'):
    filter = _input.split()[0]
    id = _input.split()[1]
    if id not in [a.id for a in apartments]:
        output += f'\nApartment with id - {id} does not exist!'
    else:
        ap = [a for a in apartments if a.id == id][0]
        if ap.occupied:
            output += f'Apartment with id - {id} is already taken!'
        elif filter == 'hire' and isinstance(ap, OfficeApartment):
            output += f'\nApartment with id - {id} is only for renting!'
        elif filter == 'rent' and isinstance(ap, LivingApartment):
            output += f'\nApartment with id - {id} is only for selling!'
        else:
            ap.occupied = True

    _input = input()
output = output.lstrip('\n')
print(output)
m = 1
if _input == 'taken':
    filter = True

else:
    filter = False
    m = -1
sorted_apartments = sorted(apartments, key=lambda a: (m * a.price, - m * a.square_meters))
filtered_apartments = [a for a in sorted_apartments if a.occupied == filter]
if len(filtered_apartments) > 0:
    report_string = '\n'.join([str(a) for a in filtered_apartments])
    print(report_string)
else:
    print('No information for this query')
