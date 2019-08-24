import re

pattern = r'\d+[A-Z][a-z]+([0-9A-Z])\1+'
regex = re.compile(pattern)
names = []
rows_number = int(input())
for i in range(rows_number):
    data = input()
    result = regex.search(data)
    name = regex.match(data)
    tmp = result.group(0)
    tmp1 = regex.fin
    print()



print(names)