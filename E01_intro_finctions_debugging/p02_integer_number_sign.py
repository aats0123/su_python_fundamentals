def print_sign(num):
    if num < 0:
        output = f"The number {num} is negative."
    elif num > 0:
        output = f"The number {num} is positive."
    else:
        output = 'The number 0 is zero.'
    return output


if __name__ == '__main__':
    number = int(input())
    message = print_sign(number)
    print(message)
