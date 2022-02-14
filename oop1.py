class Employee:
    def __init__(self):
        self.cards = []

    def lol(self):
        for j in range(2, 5):
            self.cards.append(j)

    def __iter__(self):
        return iter(self.cards)




emp_1 = Employee()
print(emp_1.cards)
emp_1.lol()
print(emp_1.cards)

for i in emp_1:
    print('hej')
