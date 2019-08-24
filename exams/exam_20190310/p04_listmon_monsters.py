from abc import ABC, abstractmethod


class BaseMonster(ABC):
    @abstractmethod
    def __init__(self, name: str, id: int, strength: int, ugliness: int):
        self.name = name
        self.id = id
        self.strength = strength
        self.ugliness = ugliness


class Hydralisk(BaseMonster):
    def __init__(self, name: str, id: int, strength: int, ugliness: int, range: str):
        BaseMonster.__init__(self, name, id, strength, ugliness)
        self.range = self.set_range(range)

    def set_range(self, value):
        if not isinstance(value, str):
            raise Exception('Range must be string')
        else:
            return value


class Zergling(BaseMonster):
    def __init__(self, name: str, id: int, strength: int, ugliness: int, speed: int):
        BaseMonster.__init__(self, name, id, strength, ugliness)
        self.speed = self.set_speed(speed)

    def set_speed(self, value):
        if not isinstance(value, int):
            raise Exception('Speed must be integer')
        else:
            return value


army = []
output = ''
_input = input()
while not _input == 'stopAddingArmy':
    try:
        monster = eval(_input)
        army.append(monster)
    except Exception as ex:
        output += f'\n{ex}'

    _input = input()

strength = sum([m.strength for m in army])
speed = sum([m.speed for m in army if m.__class__.__name__ == 'Zergling'])
zerglings_count = len(list([m for m in army if m.__class__.__name__ == 'Zergling']))
hydralisks_count = len(list([m for m in army if m.__class__.__name__ == 'Hydralisk']))

output = output.lstrip('\n') + f'\nOverall speed of army: {speed}\n' \
    f'Overall stength: {strength}\nHydralisk: {hydralisks_count}; Zergling: {zerglings_count}'

print(output)