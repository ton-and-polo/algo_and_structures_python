# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.

from random import randint

my_list = [randint(-100, 100) for _ in range(10)]
negative_list = [i for i in my_list if i < 0]

print(f'index: {negative_list.index(min(negative_list))}, element: {max(negative_list)}')
