def remove_negative(arr):
    temp_arr = []
    for element in arr:
        if element < 0:
            temp_arr += [element]
    for negative_element in temp_arr:
        arr.remove(negative_element)
    return arr


if __name__ == '__main__':
    input_arr = [int(value) for value in input().split()]

    output_arr = remove_negative(input_arr)
    if len(output_arr) > 0:
        output_arr.reverse()
        print(' '.join([str(item) for item in output_arr]))
    else:
        print('empty')