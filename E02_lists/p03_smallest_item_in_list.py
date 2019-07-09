def collect_list():
    _numbers = [int(value) for value in input().split()]
    return _numbers


if __name__ == '__main__':
    numbers = collect_list()
    min_number = min(numbers)
    print(min_number)
