def calculate_num_of_digits(num):
    digits = 0
    while num:
        num = num // 10
        digits += 1
    return digits


def sum_even_digits(num):
    sum1 = 0
    sum2 = 0
    counter = 0
    while num:
        digit = num % 10
        num = num // 10
        counter += 1
        if counter % 2:
            sum1 += digit
        else:
            sum2 += digit
    if not counter % 2:
        return sum1
    else:
        return sum2


def sum_odd_digits(num):
    sum1 = 0
    sum2 = 0
    counter = 0
    while num:
        digit = num % 10
        num = num // 10
        counter += 1
        if counter % 2:
            sum1 += digit
        else:
            sum2 += digit
    if not counter % 2:
        return sum2
    else:
        return sum1


if __name__ == '__main__':

    number = abs(int(input()))
    print(sum_even_digits(number) * sum_odd_digits(number))
