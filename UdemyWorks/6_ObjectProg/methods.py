class Car:
    wheels_number = 4

    def __init__(self, name, color, year, is_crashed):
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed

    def drive(self, city):
        print(self.name + ' is driving to ' + city)

    def change_color(self, new_color):
        self.color = new_color


mazda_car = Car('Mazda CX7', 'red', 2017, True)
mazda_car.change_color('yellow')
print(mazda_car.drive('London'))
print(mazda_car.wheels_number)
print(mazda_car.color)


class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def get_area(self):
        return self.pi * (self.radius ** 2)

    def get_circumference(self):
        return 2 * self.pi * self.radius


circle_1 = Circle()
print(circle_1.get_area())
print(circle_1.get_circumference())
circle_1 = Circle(5)
print(circle_1.get_area())
print(circle_1.get_circumference())


class BankAccount:

    def __init__(self, client_id, client_first_name, client_last_name, balance = 0.0):
        self.client_id = client_id
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name
        self.balance = balance

    def add(self, plus_sum):
        self.balance = plus_sum + self.balance

    def withdraw(self, minus_sum):
        self.balance = self.balance - minus_sum


bankAccount = BankAccount(1, 'Oleg', 'Popov', 5)
print(bankAccount.balance)
bankAccount.add(12)
print(bankAccount.balance)
bankAccount.withdraw(7)
print(bankAccount.balance)
