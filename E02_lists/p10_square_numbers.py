import math
if __name__ == '__main__':
    input_list = [int(value) for value in input().split()]
    output_list = []
    for num in input_list:
        if num > 0 and math.sqrt(num) == int(math.sqrt(num)):
            output_list += [num]

    output_list.sort(reverse=True)
    print(' '.join([str(item) for item in output_list]))