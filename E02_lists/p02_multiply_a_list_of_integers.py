def collect_list():
    values = input()
    list_values = [int(value) for value in values.split()]
    return list_values


if __name__ == '__main__':
    numbers = collect_list()
    p = int(input())
    numbers_by_p = [number * p for number in numbers]
    print(' '.join([str(value) for value in numbers_by_p]))
