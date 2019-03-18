"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""
from random import randint

row = 4
col = 4

my_list = [[randint(0, 9) for i in range(row)] for i in range(col)]

for i in range(len(my_list)):
    my_list[i].append(sum([num for num in my_list[i]]))
    print(my_list[i])
