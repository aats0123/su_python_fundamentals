def bubble_sort(elements):
    ready = False
    while not ready:
        swap_occurred = False
        for i in range(0, len(elements) - 1):
            if elements[i] > elements[i + 1]:
                elements[i], elements[i + 1] = elements[i + 1], elements[i]
                swap_occurred = True
            else:
                continue
        if not swap_occurred:
            ready = True
    return elements


if __name__ == '__main__':
    numbers = [int(value) for value in input().split()]
    numbers_sorted = bubble_sort(numbers)

    print(" ".join([str(item) for item in numbers_sorted]))
