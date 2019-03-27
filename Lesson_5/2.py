"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
import re
import collections


# Using functional programming:
num_1 = int('a2', 16)
num_2 = int('c4f', 16)

addition = re.findall(r'\w', str(hex(num_1 + num_2))[2:])
multiplication = re.findall(r'\w', str(hex(num_1 * num_2))[2:])

print(f'Functional programming\naddition: {addition}\nmultiplication: {multiplication}\n')


# Using object-oriented programming:
class MyHex:
    def __init__(self, num):
        self.num = int(num, 16)

    def __add__(self, other):
        return hex(self.num + other.num)

    def __mul__(self, other):
        return hex(self.num * other.num)


x = MyHex('a2')
y = MyHex('c4f')

print(f'Object-oriented programming\naddition: {list(x + y)[2:]}\nmultiplication: {list(x * y)[2:]}\n')


# Using collections (defaultdict):
my_collection = collections.defaultdict(list)
numbers = ['a2', 'c4f']
for i in range(len(numbers)):
    my_collection[i].append(int(numbers[i], 16))


def multiplication(my_list):
    result = 1
    for i in my_list:
        result *= i
    return result


addition = list(hex(sum([i[0] for i in my_collection.values()])))[2:]
multiplication = list(hex(multiplication([i[0] for i in my_collection.values()])))[2:]

print(f'Using collections\naddition: {addition}\nmultiplication: {multiplication}')
