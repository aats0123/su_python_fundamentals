def reverse_insert_sort(arr):
    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[i] > arr[j]:
                temp = arr[i:i + 1] + arr[j:i]
                arr[j:i + 1] = temp
    return arr


if __name__ == '__main__':
    unsorted_arr = list(map(int, input().split()))
    n = int(input())
    sorted_arr = reverse_insert_sort(unsorted_arr)
    print(*sorted_arr[:n])
