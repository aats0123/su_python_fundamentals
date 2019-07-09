counter = 3
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while counter > 0:
    temp = x[-1]
    for i in range(len(x) - 1, 0, -1):
        x[i] = x[i - 1]
    x[0] = temp
    counter -= 1

print(" ".join([str(item) for item in x]))
