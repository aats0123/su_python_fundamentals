if __name__ == '__main__':
    arr = list(map(int, input().split()))
    result_arr = [None]*1001
    for j in arr:
        if not result_arr[j]:
            result_arr[j] = 1
        else:
            result_arr[j] += 1

    for i in range(1001):
        if result_arr[i]:
            print(f'{i} -> {result_arr[i]}')