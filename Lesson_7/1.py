"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
import random

my_list = [random.randint(-100, 100) for i in range(10)]


def bubble_sort(list):

    length_list = len(list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length_list):
            if list[i] < list[i+1]:
                list[i+1], list[i] = list[i], list[i + 1]
                sorted = False
        if sorted:
            # Break the loop if there's no swap
            break

    return list


print(bubble_sort(my_list))
