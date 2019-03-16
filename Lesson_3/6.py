"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

my_list = [8, 3, 15, 6, 4, 2]

result = [i for i in my_list if i != max(my_list) and i != min(my_list)]
print(f'The sum of all items in the array without max and min is: {sum(result)}')
