if __name__ == '__main__':
    arr = list(map(int, input().split()))
    sorted_arr = arr[:1]
    for i in range(1, len(arr)):
        for j in range(0, len(sorted_arr)):
            inserted = False
            if arr[i] < sorted_arr[j]:
                sorted_arr = sorted_arr[:j] + [arr[i]] + sorted_arr[j:]
                inserted = True
                break
        if not inserted:
            sorted_arr.append(arr[i])

    print(*sorted_arr)
