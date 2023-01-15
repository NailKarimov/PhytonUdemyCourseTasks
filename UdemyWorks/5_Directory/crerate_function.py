def print_greeting():
    '''
    :return: None
    '''
    print('Hello')


print_greeting()


def print_greeting_with_name(name='Name'):
    '''
    :param name
    :return:
    '''
    print('Hello ' + name + '!')


print_greeting_with_name()


def sum_of_true_numbers(a=0, b=0):
    '''
    :param a:
    :param b:
    :return:
    '''
    return a + b


x = sum_of_true_numbers(1, 1)
print(x)


def is_hello_in_text(text):
    if 'hello' in text.lower():
        return True
    else:
        return False


print(is_hello_in_text('Hello everyone!'))


def is_hello_in_text2(text):
    return 'hello' in text.lower()


print(is_hello_in_text2('everyone!'))

'---------------------------------------------------------------------------------------'


def cat_voice():
    """
    :return: None
    """
    print('Meow!')


cat_voice()


def dog_voice():
    """
    :return:
    """
    print('Woof!')


dog_voice()

for voice in range(2):
    cat_voice()
    dog_voice()


def get_voice(voice):
    """
    :return:
    """
    print(voice + '!')


voice = input('Enter any voice: ')
get_voice(voice)


def oddList(x, y):
    """
    :return: list
    """
    mylist = []
    for num in range(x, y + 1):
        if (num % 2) != 0:
            mylist.append(num)
    print(mylist)


numberX = int(input('Enter any from number '))
numberY = int(input('Enter any till number '))
oddList(numberX, numberY)


def oddListComp(x, y):
    """
    :return: list
    """
    mylist = [number for number in range(x, y + 1) if (number % 2) != 0]
    print(mylist)


numberX = int(input('Enter any from number '))
numberY = int(input('Enter any till number '))
oddListComp(numberX, numberY)
