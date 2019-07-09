if __name__ == '__main__':
    input_list = [int(value) for value in input().split()]
    input_list.sort()
    print(' <= '.join(str(item) for item in input_list))
