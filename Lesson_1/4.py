"""
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой
символ алфавита от 'a' до 'f' включительно.
"""
import random
import string

print('[1] - random integer\n[2] - random real number\n[3] - random char')
user_input = int(input('Enter num:\n'))
user_range = input('Enter range (x,y): ')
x = int(user_range.split(',')[0])
y = int(user_range.split(',')[1])

if user_input == 1:
    print(random.randint(x, y))
elif user_input == 2:
    print(random.uniform(x, y))
elif user_input == 3:
    # string.punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    print(string.punctuation[random.randint(x, y)])