input_list = [int(num) for num in input().split()]


def multiply(data_list, params):
    if params[0] == 'list':
        data_list = data_list * int(params[1])
        return data_list
    else:
        m = int(params[0])
        n = int(params[1])
        data_list = [el * n if el == m else el for el in data_list]
        return data_list


def contains(data_list, params):
    if int(params[0]) in data_list:
        print('True')
    else:
        print('False')


def add(data_list, params):
    if ',' in params[0] :
        params = params[0].split(',')
        new_lest = [int(el) for el in params]
        data_list.extend(new_lest)
        return data_list
    else:
        new_element = int(params[0])
        data_list.append(new_element)
        return data_list


_input = input()
while not _input == 'END':
    command = _input.split()[0]
    params = _input.split()[1:]
    if command == 'multiply':
        input_list = multiply(input_list, params)
    elif command == 'contains':
        contains(input_list, params)
    elif command == 'add':
        input_list = add(input_list, params)
    _input = input()

data_list = sorted(input_list)
output = ' '.join(str(el) for el in data_list)
print(output)