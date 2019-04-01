"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""
from random import randint
from statistics import median


my_list = [randint(-10, 10) for i in range(randint(1, 100))]


# Built-in solution (median()):
print(median(my_list))


# Cocktail shaker and my_median solution:
def shaker_sort(my_list):
    left = 0
    right = len(my_list) - 1

    swap = False
    while not swap and right - left > 1:
        swap = True

        for i in range(right, left, -1):
            if my_list[i - 1] > my_list[i]:
                my_list[i], my_list[i - 1] = my_list[i - 1], my_list[i]
                swap = False
        left += 1

        for i in range(left, right):
            if my_list[i + 1] < my_list[i]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                swap = False
        right -= 1

    return my_list


def my_median(my_list):
    if len(my_list) == 1:
        return my_list[0]

    my_list = shaker_sort(my_list)

    x = my_list[(len(my_list) - 1) // 2]
    y = my_list[(len(my_list)) // 2]
    diff = y - x

    if len(my_list) % 2 == 0:
        if diff == 0:
            result = my_list[len(my_list)//2]
        elif abs(diff) == 1 or abs(diff) >= 3:
            result = x + (diff/2)
        elif abs(diff) < 3:
            result = diff

    elif len(my_list) % 2 != 0:
        result = my_list[len(my_list)//2]

    return float(result)


print(my_median(my_list))
