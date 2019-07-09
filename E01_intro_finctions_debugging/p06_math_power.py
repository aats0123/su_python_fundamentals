def power(base, _power):
    result = base**_power
    return result


if __name__ == '__main__':

    base = float(input())
    _power = int(input())
    result = power(base, _power)
    print(result)
