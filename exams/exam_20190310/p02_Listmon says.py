def c_set(_list):
    set_list = set(_list)
    if len(set_list) == len(_list):
        return 'It is a set'
    else:
        unique_list = []
        for el in _list:
            if el not in unique_list:
                unique_list.append(el)
            else:
                continue
    return unique_list.__str__()


def c_filter(_list, command):
    num = 0
    if command == 'odd':
        num = 1
    new_list = [el for el in _list if el % 2 == num]
    if len(new_list) > 0:
        return [el for el in _list if el % 2 == num].__str__()
    else:
        return None


def c_multiply(_list, number):
    return [el * number for el in _list].__str__()


def c_divide(_list, num):
    if num == 0:
        return 'ZeroDivisionError caught'
    else:
        return [el / num for el in _list].__str__()


def c_slice(_list, n, m):
    if (m > len(_list) - 1) or (n > len(_list)):
        return 'IndexError caught'
    else:
        cur_list = _list
        return cur_list[n:m + 1].__str__()


def c_sort(_list):
    curr_list = _list[:]
    curr_list.sort()
    return curr_list.__str__()


def c_reverse(_list):
    curr_list = _list[:]
    curr_list.reverse()
    return curr_list.__str__()


command_dict = {
    'set': c_set,
    'filter': c_filter,
    'multiply': c_multiply,
    'divide': c_divide,
    'slice': c_slice,
    'sort': c_sort,
    'reverse': c_reverse
}

_list = input().split()
_list = [int(el) for el in _list if el != ' ']
_input = input()
count = 0
output = ''

while not _input == 'exhausted':
    count += 1
    _input = _input.split()
    command = _input[0]
    if len(_input) == 2:
        try:
            param = int(_input[1])
        except:
            param = _input[1]
        message = command_dict[command](_list, param)
    elif len(_input) == 3:
        num1 = int(_input[1])
        num2 = int(_input[2])
        message = command_dict[command](_list, num1, num2)
    else:
        message = command_dict[command](_list)
    if  message:
        output += '\n' + message

    _input = input()

output += f'\nI beat It for {count} rounds!'

print(output)
