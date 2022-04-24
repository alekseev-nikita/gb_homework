class Worker:
    name, surname, position, income = None, None, None, None


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname.capitalize()
        self.position = position.capitalize()
        self.income = {'wage': wage, 'bonus': bonus}

    def get_full_name(self):
        return f'{self.name} {self.surname} - {self.position}'

    def get_total_income(self):
        return self.income.get('wage') + self.income.get('bonus')


p1 = Position('Ivan', 'Ivanov', 'Teacher', 500, 270)
p2 = Position('Dima', 'Dmitri', 'Driver', 800, 450)
print(p1.get_full_name())
print(p1.get_total_income())
print(p2.get_full_name())
print(p2.get_total_income())
