def average(lst: list):
    return sum(lst) / len(lst)


_input = input()
while not _input == "stop playing":
    _input = _input.split()
    _input = list(filter(lambda el: el != ' ', _input))
    _input = [int(el) for el in _input]

    test_set = set(_input)
    message = ''

    if len(test_set) == len(_input):
        output = sorted([el + 2 if (el % 2 == 0) else el for el in _input])
        message = 'Unique list: ' + ','.join([str(el) for el in output]) + f'\nOutput: {average(output):.2f}'
    else:
        output = sorted([el + 3 if (el % 2 == 1) else el for el in _input])
        message = 'Non-unique list: ' + ':'.join([str(el) for el in output]) + f'\nOutput: {average(output):.2f}'

    print(message)

    _input = input()
