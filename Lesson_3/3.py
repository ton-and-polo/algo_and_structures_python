# 3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

my_list = [8, 3, 15, 6, 4, 2]

a, b = my_list.index(max(my_list)), my_list.index(min(my_list))
my_list[a], my_list[b] = my_list[b], my_list[a]

print(f'Swapped min and max elements: {my_list}')
