if __name__ == '__main__':
    nums = [int(value) for value in input().split()]
    message = ''
    for i in range(0,len(nums)):
        if i % 2 and nums[i] % 2:
            if not i == len(nums) - 1:
                message += f'Index {i} -> {nums[i]}\n'
            else:
                message += f'Index {i} -> {nums[i]}'

    print(message)