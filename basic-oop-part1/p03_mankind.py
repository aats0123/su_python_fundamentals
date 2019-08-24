class Human:
    def __init__(self, f_name: str, l_name: str):
        self.first_name = f_name
        self.last_name = l_name

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        if not value[0].isupper():
            print('Expected upper case letter! Argument: firstName')
            exit(0)
        elif not len(value) > 3:
            print('Expected length at least 4 symbols! Argument: firstName')
            exit(0)
        else:
            self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        if not value[0].isupper():
            print('Expected upper case letter! Argument: lastName')
            exit(0)
        elif not len(value) > 2:
            print('Expected length at least 3 symbols! Argument: lastName')
            exit(0)
        else:
             self.__last_name = value

    def __str__(self):
        return f"First Name: {self.first_name}\nLast Name: {self.last_name}"


class Student(Human):
    def __init__(self, f_name: str, l_name: str, faculty_number: str):
        Human.__init__(self, f_name, l_name)
        self.faculty_number = faculty_number

    @property
    def faculty_number(self):
        return self.__faculty_number

    @faculty_number.setter
    def faculty_number(self, value):
        if not 10 >= len(value) >= 5 or not value.isalnum():
            print('Invalid faculty number!')
            exit(0)
        else:
            self.__faculty_number = value

    def __str__(self):
        return Human.__str__(self) + f"\nFaculty number: {self.faculty_number}"


class Worker(Human):
    def __init__(self, f_name: str, l_name: str, w_salary: float, d_hours: float):
        Human.__init__(self, f_name, l_name)
        self.week_salary = w_salary
        self.hours_per_day = d_hours
        self.salary_per_hour = self.week_salary / (self.hours_per_day * 5)

    @property
    def week_salary(self):
        return self.__week_salary

    @week_salary.setter
    def week_salary(self, value):
        if value < 10:
            print('Expected value mismatch! Argument: weekSalary')
            exit(0)
        else:
            self.__week_salary = value

    @property
    def hours_per_day(self):
        return self.__hours_per_day

    @hours_per_day.setter
    def hours_per_day(self, value):
        if not 12 >= value >= 1:
            print('Expected value mismatch! Argument: workHoursPerDay')
            exit(0)
        else:
            self.__hours_per_day = value

    def __str__(self):
        return \
            Human.__str__(self) + \
            f"\nWeek Salary: {self.week_salary:.2f}" + \
            f"\nHours per day: {self.hours_per_day:.2f}\nSalary per hour: {self.salary_per_hour:.2f}"


student_info = list(input().split())
student = Student(student_info[0], student_info[1], student_info[2])
worker_info = list(input().split())
worker = Worker(worker_info[0], worker_info[1], float(worker_info[2]), float(worker_info[3]))

print(student)
print()
print(worker)
