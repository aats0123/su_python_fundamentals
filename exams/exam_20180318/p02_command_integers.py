state_ints = [int(num) for num in input().split()]
command_ints = [int(num) for num in input().split()]
for command in command_ints:
    temp = abs(command)
    if temp % 2:
        for i in range(len(state_ints)):
            if state_ints[i] % 2:
                state_ints[i] = state_ints[i] // temp
    else:
        for i in range(len(state_ints)):
           if not state_ints[i] % 2:
               state_ints[i] = state_ints[i] * temp

    if command > 0:
        for i in range(len(state_ints)):
            if state_ints[i] > 0:
                state_ints[i] += command
    else:
        for i in range(len(state_ints)):
            if state_ints[i] < 0:
                state_ints[i] += command


print(state_ints)

