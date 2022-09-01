def is_cat_here(*args):
    """
    :param args:
    :return: boolean
    """
    bool = False
    for words in args:
        if words.upper() == 'CAT': bool = True
    return bool


print(is_cat_here('cow', 'horse', 'dog', 'cate', 'CAte', 'cAt', 'cat'))


def is_item_here(item, *args):
    """
    :param item:
    :param args:
    :return: boolean
    """
    bool = False
    for words in args:
        if words == item: bool = True
    return bool


print(is_item_here('cow', 'horse', 'dog', 'cate', 'CAte', 'cow', 'cat'))


def your_favorite_color(**kwargs):
    if not 'color' in kwargs:
        print('My favorite color is {}'.format(kwargs['my_color']) + ' what is your favorite color?')
    else:
        print('My favorite color is {}'.format(kwargs['my_color']) +
              ' but {}'.format(kwargs['color']) + ' is also pretty good!')


your_favorite_color(my_color='red')
your_favorite_color(my_color='red', color='blue')
