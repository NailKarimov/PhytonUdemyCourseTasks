# Generators are iterators
# Generators can be created with generator functions
# Generators can be created with generator expressions


# def my_function(x):
#     return x
#
#
# print(my_function(4))


# def count_up_to(x):
#     count = 1
#     while count <= x:
#         yield count
#         count += 1
#
#
# print(count_up_to(4))


# counter = count_up_to(4)
# # print(counter.__next__())
# # print(counter.__next__())
# # print(counter.__next__())
# # print(counter.__next__())
# # print(counter.__next__())
#
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

# counter = count_up_to(10)
# print(list(count_up_to(7)))
#
# # for number in counter:
# #     print(number)
#
# counter.__next__()
# counter.__next__()
# counter.__next__()
#
# for number in counter:
#     print(number)

# #=================================================================================================================
# def get_week_day(x, week_tuple_list):
#     count = 0
#     while count <= x:
#         yield week_tuple_list[count]
#         count += 1
#
#
# week_tuple = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
# current_day = get_week_day(len(week_tuple), week_tuple)
#
# print(current_day.__next__())  # 'Sunday'
# print(current_day.__next__())  # 'Monday'
# print(current_day.__next__())  # 'Tuesday'
# print(current_day.__next__())  # 'Wednesday'
# print(current_day.__next__())  # 'Thursday'
# print(current_day.__next__())  # 'Friday'
# print(current_day.__next__())  # 'Saturday'
#
# #=================================================================================================================
#
# def get_week_day():
#     week = [
#         "Sunday",
#         "Monday",
#         "Tuesday",
#         "Wednesday",
#         "Thursday",
#         "Friday",
#         "Saturday",
#     ]
#     for day in week:
#         yield day
# #=================================================================================================================


# def even_odd():
#     even = ['even', 'odd']
#     count = 1
#     while count <= count:
#         for number in even:
#             yield number
#
#
# counter = even_odd()
# print(counter.__next__())
# print(counter.__next__())
# print(counter.__next__())
# print(counter.__next__())
# print(counter.__next__())
# print(counter.__next__())
# print(counter.__next__())
# print(counter.__next__())
# print(counter.__next__())
# print(counter.__next__())
# print(counter.__next__())
# print(counter.__next__())

# #=================================================================================================================
# def even_odd():
#     value = 'even'
#     while True:
#         yield value
#         if value == 'even':
#             value = "odd"
#         else:
#             value = "even"

# #=================================================================================================================

#
# def hello(func):
#     def wrapper():
#         func()
#     return wrapper
#
#
# @hello
# def hello_from_decorator():
#     print("Hello from decorator!")
#
#
# hello_from_decorator()

from functools import wraps


def hello_from_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return str(result) + ' Hello from decorator!'
    return wrapper


@hello_from_decorator
def some_func():
    return 3


print(some_func())
