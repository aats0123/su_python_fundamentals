if __name__ == '__main__':
    input_lists = input().split('|')
    input_lists.reverse()
    temp_list = []
    for _list in input_lists:
        temp_list += _list.split()

    print(' '.join(temp_list))