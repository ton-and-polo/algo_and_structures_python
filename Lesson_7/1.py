"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
import random

my_list = [random.randint(-100, 100) for i in range(10)]


def bubble_sorting(list):
    index = 1
    while index < len(list):
        for i in range(len(list)-1):
            if list[i] < list[i + 1]:
                list[i + 1], list[i] = list[i], list[i + 1]
        index += 1

    return list


print(bubble_sorting(my_list))
