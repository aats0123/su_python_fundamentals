from datetime import datetime as dt

exam_date = dt(2018, 8, 26)
_input = input().split('-')
year = int(_input[0])
month = int(_input[1])
day = int(_input[2])
cur_date = dt(year, month, day)
difference = (cur_date - exam_date).days
message = 'Passed'
if difference == 0:
    message = 'Today date'
elif difference > 0:
    message = f'{difference + 1} days left'

print(message)