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


class Truck(Car):
    wheels_number = 6

    def __init__(self, name, color, year, is_crashed):
        Car.__init__(self, name, color, year, is_crashed)
        print('Truck is created')

    def drive(self, city):
        print('Truck ' + self.name + ' is driving to ' + city)

    def load_cargo(self, weight):
        print('The cargo is loaded. Weight is ' + str(weight) + 'kg')


man_track = Truck('Man', 'white', 2015, False)
man_track.drive('New York')
print(man_track.wheels_number)
man_track.load_cargo(2000)


# Polymorphism

class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' is saing woof')


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' is saing meow')


class Mouse:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' is saing pe-pe-pe')


spike = Dog('Spike')
tom = Cat('Tom')
jerry = Mouse('Jerry')

pet_list = [spike, tom, jerry]

for pet in pet_list:
    pet.speak()


##---------------------------------------------------------------

class GameCharacter:
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level

    def speak(self):
        print('Hi, my name is ' + self.name)


class Villane(GameCharacter):
    def __init__(self, name, health, level):
        GameCharacter.__init__(self, name, health, level)

    def speak(self):
        print('Hi, my name is ' + self.name + ' and I will kill you')

    def kill(self, other):
        other.health = 0
        print('Bang-bang, now youre dead')


firstGame = GameCharacter('Chess', 10, 4)
firstGame.speak()
secondGame = Villane('Ping - pong', 1, 54)
secondGame.speak()
secondGame.kill(firstGame)
print(firstGame.health)
