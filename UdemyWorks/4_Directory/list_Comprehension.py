greetings = ['hello', 'hi', 'hey', 'hola']

letter_list = []
for char in greetings:
    if len(char) > 1:
        letter_list.append(char[1])
print(letter_list)

letter_list2 = []
greetings_list = [letter_list2.append(char[1]) for char in greetings]
print(letter_list2)

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

digits_list = []
for number in digits:
    if (number % 2) != 0:
        digits_list.append(number)
print(digits_list)

digits_list2 = [number for number in digits if (number % 2) != 0]
print(digits_list2)
