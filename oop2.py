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

print(Employee.num_of_emps)
emp_1 = Employee('Axel', 'Qvarnström', '50000 kr')
emp_2 = Employee('alex', 'Lundh', '10000 kr')

# print(Employee.__dict__)



emp_1.raise_amount = 1.05
print(emp_1.__dict__)
emp_1.set_raise_amt(1.08)

print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)

print(Employee.num_of_emps)
