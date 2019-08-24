def swap(_list: list, index1: int, index2: int):
    if 0 > index1 or index1 > (len(_list) - 1) or 0 > index2 or index2 > (len(_list) - 1):
        return _list.__str__()
    else:
        _list[index1], _list[index2] = _list[index2], _list[index1]
        return _list.__str__()


def enumerate_list(_list: list):
    return list(enumerate(_list)).__str__()


def get_divisible_by(_list: list, num: int):
    return [n for n in _list if n % num == 0].__str__()


_list = [int(el) for el in input().split()]
output = ''
_input = input()
counter = 0
while not _input == 'end':
    _input = _input.split()
    counter += 1
    command = _input[0]
    if command == 'swap':
        index1 = int(_input[1])
        index2 = int(_input[2])
        output += '\n' + swap(_list, index1, index2)
    elif command == 'enumerate_list':
        output += '\n' + enumerate_list(_list)
    elif command == 'max':
        output += '\n' + str(max(_list))
    elif command == 'min':
        output += '\n' + str(min(_list))
    elif command == 'get_divisible':
        if _input[1] == 'by':
            output += '\n' + get_divisible_by(_list, int(_input[2]))
        else:
            counter -= 1
            _input = input()
            continue
    else:
        counter -= 1
        _input = input()
        continue

    _input = input()

output = output.lstrip('\n') + f'\n{counter}'
print(output)
