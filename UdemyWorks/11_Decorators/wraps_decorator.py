from functools import wraps


def print_function_data(function):
    """
    This is decorator function
    :param function:
    :return:
    """
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"You are using {function.__name__}")
        print(f"Function documentation {function.__doc__}")
        return function(*args, **kwargs)
    return wrapper


@print_function_data
def squares_sum(a, b):
    """

    :param a: first number
    :param b: second number
    :return: sum of squares first and second numbers: (a * a + b * b)
    """
    return a * a + b * b


# print(squares_sum(2, 3))
print(squares_sum.__doc__)
print(squares_sum.__name__)
# help(squares_sum)
# #=================================================================================================================


def print_args(function):
    """

    :return:
    """
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(print_args().__doc__)
        print(print_args().__name__)
        return function(*args, **kwargs)
    return wrapper


print(print_args(squares_sum).__doc__)

# #=================================================================================================================

def print_args(function):
    """

    :return:
    """
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(print_args().__doc__)
        print(print_args().__name__)
        return function(*args, **kwargs)
    return wrapper


print(print_args(squares_sum).__doc__)

# #=================================================================================================================
