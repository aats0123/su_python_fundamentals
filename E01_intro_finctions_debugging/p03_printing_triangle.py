def print_upper(num):
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            if not j == i:
                print(str(j) + ' ', end='')
            else:
                print(str(j))


def print_lower(num):
    for i in range(num, 0, -1):
        for j in range(1, i):
            if not j == i - 1:
                print(str(j) + ' ', end='')
            else:
                print(str(j))


if __name__ == '__main__':
    size = int(input())
    print_upper(size)
    print_lower(size)
