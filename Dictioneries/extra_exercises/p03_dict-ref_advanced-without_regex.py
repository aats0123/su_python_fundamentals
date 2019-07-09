if __name__ == '__main__':
    dictionary = {}
    _input = input()
    while _input != 'end':
        key = _input.split(' -> ')[0]
        token = _input.split(' -> ')[1]
        if token[0].isdigit():
            values = token.split(', ')
            if key not in dictionary.keys():
                dictionary[key] = values
            else:
                dictionary[key].extend(values)
        else:
            if token in dictionary.keys():
                dictionary[key] = dictionary[token].copy()

        _input = input()

    for kvp in dictionary.items():
        values = ', '.join([i for i in kvp[1]])
        print(f'{kvp[0]} === {values}')