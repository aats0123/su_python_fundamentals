def collect_list(n):
    inp_list = []
    for i in range(0, n):
        inp_list += [int(input())]
    return inp_list


if __name__ == '__main__':
    list_size = int(input())
    in_list = collect_list(list_size)
    list_sum = sum(in_list[:])
    print(list_sum)
