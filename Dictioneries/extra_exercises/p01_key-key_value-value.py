def list_search(_list, _string):
    result = []
    for i in range(len(_list)):
        if _list[i].find(_string) is not -1:
            result.append(i)
    return result


if __name__ == '__main__':
    key_values = {}
    key = input()
    value = input()
    n = int(input())
    for j in range(n):
        _input = input().split(' => ')
        curr_key = _input[0]
        curr_value = _input[1].split(';')
        key_values[curr_key] = curr_value

    for kvp in key_values.items():
        matches = list_search(kvp[1], value)
        if kvp[0].find(key) is not -1:
            print(f'{kvp[0]}:')
            if len(matches) > 0:
                print('-' + '\n-'.join([str(kvp[1][i]) for i in matches]))
