class Employer:
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary

    def introduce(self):
        print(f"Name: {self.name}, Surname: {self.surname}, Salary: {self.salary}")

emp1 = Employer("Bob", "Winkel", 5000)

emp1.introduce()


class Manager(Employer):
    def __init__(self, name, surname, salary, department):
        super().__init__(name,surname,salary)
        self.department = department

emp2 = Manager("Tom", "Tooth", 3900, "Data")

emp2.introduce()

class Intern(Employer):
    def __init__(self, name, surname, salary=2000):
        super().__init__(name,  surname, salary)

stg1 = Intern("Suzan", "Qwerty")

stg1.introduce()
