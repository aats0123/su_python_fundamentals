if __name__ == '__main__':
    SEPARATOR = '\n===================='
    employees_age = {}
    employees_salary = {}
    employees_position = {}

    employee_info = input()

    while employee_info != 'filter base':
        employee_name = employee_info.split(' -> ')[0]
        extra_info = employee_info.split(' -> ')[1]
        if extra_info.isdigit():
            employees_age[employee_name] = int(extra_info)
        else:
            try:
                salary = float(extra_info)
                employees_salary[employee_name] = salary
            except:
                employees_position[employee_name] = extra_info

        employee_info = input()

    required_info = input()
    if required_info == 'Age':
        print('\n'.join(
            [f'Name: {name}\n{required_info}: {employees_age[name]}' + SEPARATOR for name in employees_age.keys()]))
    elif required_info == 'Salary':
        print('\n'.join([f'Name: {name}\n{required_info}: {employees_salary[name]}' + SEPARATOR for name in
                         employees_salary.keys()]))
    else:
        print('\n'.join([f'Name: {name}\n{required_info}: {employees_position[name]}' + SEPARATOR for name in
                         employees_position.keys()]))

