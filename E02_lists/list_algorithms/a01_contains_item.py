if __name__ == '__main__':
    nums = [int(value) for value in input().split()]
    number = int(input())
    matchExists = False

    for num in nums:
        if not num == number:
            continue
        else:
            matchExists = True
            break

    if matchExists:
        print('yes')
    else:
        print('no')