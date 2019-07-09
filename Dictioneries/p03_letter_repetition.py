if __name__ == '__main__':
    symbols = list(input())
    occurrences = {}
    for symbol in symbols:
        occurrences[symbol] = occurrences.get(symbol, 0) + 1

    print('\n'.join([f'{kvp[0]} -> {kvp[1]}' for kvp in occurrences.items()]))
