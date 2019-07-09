if __name__ == '__main__':
    _input = input()
    phonebook = {}
    while _input != 'Over':
        info = _input.split(' : ')
        if info[0].isdigit():
            name = info[1]
            phone_number = info[0]
        else:
            name = info[0]
            phone_number = info[1]
        phonebook[name] = phone_number
        _input = input()
    print('\n'.join([f'{name} -> {phonebook[name]}' for name in sorted(phonebook.keys())]))