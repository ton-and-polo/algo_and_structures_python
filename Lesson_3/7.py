"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""
my_list = [8, 3, 15, 6, 4, 2, 5, 3]

min_1 = min(my_list)
min_1_frequency = len([i for i in my_list if i == min(my_list)])


if min_1_frequency > 1:
    print(f'min: {min_1}, frequency: {min_1_frequency}')
else:
    print(f'min_1: {min_1}, frequency: {min_1_frequency}')
    min_2 = min([i for i in my_list if i != min_1])
    min_2_frequency = len([i for i in my_list if i == min_2])
    print(f'min_2: {min_2}, frequency: {min_2_frequency}')
