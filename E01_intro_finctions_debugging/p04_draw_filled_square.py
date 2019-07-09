def print_edge_line(n):
    for i in range(1, 2*n):
        print('-', end='')
    print('-')


def print_core_line(n):
    print('-', end='')
    for i in range(1, 2 * n - 1):
        if not (i % 2):
            print('/', end='')
        else:
            print('\\', end='')
    print('-')

if __name__ == '__main__':

    size = int(input())

    for i in range(0, size):
        if i == 0 or i == size -1:
            print_edge_line(size)
        else:
            print_core_line(size)
