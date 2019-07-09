if __name__ == '__main__':
    nums = [int(value) for value in input().split()]
    positive_nums = []
    for num in nums:
        if num >= 0:
            positive_nums.append(num)
    if len(positive_nums) > 0:
        positive_nums.reverse()
        message = ' '.join([str(item) for item in positive_nums])
    else:
        message = 'empty'
    print(message)