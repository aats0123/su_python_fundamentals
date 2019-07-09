if __name__ == '__main__':
    input_string = input().split()
    rotated_string = []
    rotated_string += input_string[-1:]
    for i in range(0, len(input_string) - 1):
        rotated_string += input_string[i:i+1]
    print(' '.join(rotated_string))
