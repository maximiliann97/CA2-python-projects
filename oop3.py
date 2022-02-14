class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        return int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday == 5 or day.weekday == 6:
            return False
        return True


emp_1 = Employee('Axel', 'Qvarnstrom', 50000)
emp_2 = Employee('Albin', 'Josefsson', 50000)

emp_str_1 = 'Mohammed-Elneny-20000 kr'
emp_str_2 = 'Josef-Fares-26000'
emp_str_3 = 'Lisa-Ajax-90000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.fullname())


import datetime
my_date = datetime.date(2022, 2, 14)
print(Employee.is_workday(my_date))




