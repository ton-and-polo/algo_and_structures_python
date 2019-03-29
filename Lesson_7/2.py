"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""
import random


my_list = [random.randint(0, 50) for i in range(10)]


def merge_sort(list):

    if len(list) > 1:

        middle = len(list)//2
        left = list[:middle]
        right = list[middle:]

        merge_sort(left)
        merge_sort(right)

        i = 0  # index left
        j = 0  # index right
        k = 0  # index list

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1

    return list


print(merge_sort(my_list))
