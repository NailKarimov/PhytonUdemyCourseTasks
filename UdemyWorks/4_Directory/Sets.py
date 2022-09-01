rainbow_colors = {'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'}

print(rainbow_colors)
print(type(rainbow_colors))

empty_set = set()
print(empty_set)
print(type(empty_set))

number_list = [1, 43, 56]
text_tupel = ('dfds', 'asdsa', 'asdas')
set_from_list = set(number_list)
set_from_tuple = set(text_tupel)

print(set_from_list)
print(set_from_tuple)

set_from_list.add(777)
set_from_tuple.add('sfdsdafsd')

print(set_from_list)
print(set_from_tuple)

set_from_list.pop()
set_from_list.remove(43)
set_from_list.discard(43)

print(set_from_list)
print(set_from_tuple)

car_manufactures = {'toyota', 'bmw', 'volkswagen', 'mercedes', 'mazda', 'volvo', 'ford'}
print(car_manufactures)
print(type(car_manufactures))

big_text = 'Создайте множество при помощи функции'
text = set(big_text)
print(text)
print(type(text))
