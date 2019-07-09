if __name__ == '__main__':
    numbers = [float(number) for number in input().split()]
    counter = {}
    for number in numbers:
        counter[number] = counter.get(number, 0) + 1

    sorted_numbers = sorted(list(counter.keys()))

    for num in sorted_numbers:
        print(f'{num} -> {counter[num]} times')
