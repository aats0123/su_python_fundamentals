def swap_list_elements(elements):
    for i in range(0, len(elements) // 2):
        elements[i], elements[-i-1] = elements[-i-1], elements[i]
    return elements


if __name__ == '__main__':

    numbers = [int(value) for value in input().split()]
    reversed_list = swap_list_elements(numbers)

    print(" ".join([str(item) for item in reversed_list]))
