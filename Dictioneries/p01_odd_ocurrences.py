if __name__ == '__main__':
    words = [value.lower() for value in input().split()]
    result = {}
    for word in words:
        result[word] = result.get(word, 0) + 1

    print(', '.join([kvp[0] for kvp in result.items() if kvp[1] % 2]))