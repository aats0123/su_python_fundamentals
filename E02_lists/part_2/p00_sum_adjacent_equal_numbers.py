if __name__ == '__main__':
    arr = list(map(float, input().split()))
    exist_equal_adjacent = True

    while exist_equal_adjacent:
        exist_equal_adjacent = False
        for i in range(len(arr) - 1):
            if arr[i] == arr[i+1]:
                arr = arr[:i] + [arr[i] * 2] + arr[i+2:]
                exist_equal_adjacent = True
                break

    print(*arr)
