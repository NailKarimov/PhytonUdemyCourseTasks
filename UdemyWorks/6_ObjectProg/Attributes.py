class Car:
    def __init__(self, name, color, year):
        self.name = name
        self.color = color
        self.year = year


mazda_car = Car(name='Mazda CX7', color='red', year=2017)

print(mazda_car.name)

bmw_car = Car(name='BMW', color='black', year=2018)

print(bmw_car.name)
print(bmw_car.year)


class BlogPost:
    def __init__(self, user_name, text, number_of_likes):
        self.user_name = user_name
        self.text = text
        self.number_of_likes = number_of_likes


first_user = BlogPost(user_name='Sergey', text='We love music', number_of_likes=4)
second_user = BlogPost(user_name='Oleg', text='I have a car', number_of_likes=12)
second_user.number_of_likes = second_user.number_of_likes * 4

print(first_user.number_of_likes)
print(second_user.number_of_likes)
