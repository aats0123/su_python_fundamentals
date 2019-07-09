if __name__ == '__main__':
    arr = list(map(int, input().split()))
    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[i] < arr[j]:
                temp = arr[i:i+1] + arr[j:i]
                arr[j:i+1] = temp
    print(*arr)
