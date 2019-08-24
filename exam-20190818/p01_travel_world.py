n = int(input())
m = float(input())
counter = 0
output = ''

for i in range(n):
    message = input()
    item = 'item'
    if message.isdigit():
        decoded_message = ''
        for j in range(0, len(message) - 1, 2):
            cur_char = chr(int(message[j] + message[j+1]))
            decoded_message += cur_char
        counter += 1

    elif message.isalpha():
        decoded_message = message[::-1]
        item = 'location'
        counter += 1
    else:
        continue
    output += f'Reviewing {item} - {decoded_message}\n'

output += f'{counter} reviews have been made this month. Salary: {counter * m:.2f}'
print(output)
