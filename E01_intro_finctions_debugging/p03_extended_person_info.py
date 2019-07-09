name = input()
age = int(input())
town = input()
salary = float(input())
age_range = None
salary_range = None

if age < 18:
    age_range = 'teen'
elif 18 <= age < 70:
    age_range = 'adult'
else:
    age_range = 'elder'

if salary < 500:
    salary_range = 'low'
elif 500 <= salary < 2000:
    salary_range = 'medium'
else:
    salary_range = 'high'

output = f'Name: {name}\n' + f'Age: {age}\n' + f'Town: {town}\n' + f'Salary: ${salary:.2f}\n' +\
f'Age range: {age_range}\n' + f'Salary range: {salary_range}'

print(output)