def smallest_element(elements):
    min_element = elements[0]
    for element in elements:
        if element < min_element:
            min_element = element
        else:
            continue
    return min_element


if __name__ == '__main__':
    numbers = [int(value) for value in input().split()]
    smallest = smallest_element(numbers)
    print(str(smallest))
