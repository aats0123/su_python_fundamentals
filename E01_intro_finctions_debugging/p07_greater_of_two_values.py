def greater_value(_type, str1, str2):
    if _type == 'int':
        return max(int(str1), int(str2))

    else:
        return max(str1, str2)


if __name__ == '__main__':
    _type = input()
    value1 = input()
    value2 = input()

    print(greater_value(_type, value1, value2))

