from functools import wraps


def prohibit_more_than_2_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if len(args) <= 2:
            result = func(*args, **kwargs)
            return str(result)
        else:
            return valueError()
    return wrapper


@prohibit_more_than_2_args
def some_func(first, second):
    return 3


def valueError():
    return "Function must have less than 3 arguments!"


print(some_func("First", "Second"))

# #=================================================================================================================


def prohibit_more_than_2_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if len(args) < 3:
            return func(*args, **kwargs)
        else:
            raise ValueError('Function must have less than 3 arguments!')
    return wrapper


@prohibit_more_than_2_args
def some_func(a, b, c):
    return 'Foo'


print(some_func(1, 2, 3))

