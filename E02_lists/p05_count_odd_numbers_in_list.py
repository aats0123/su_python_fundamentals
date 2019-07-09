if __name__ == '__main__':
    nums = [int(value) for value in input().split()]
    counter = 0
    for num in nums:
        if num % 2:
            counter += 1

    print(counter)