"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""
from memory_profiler import profile


@profile
def reverse(n):
    reverse_list = list(range(n))
    result = list()
    max_index = len(reverse_list) - 1
    for index in range(len(reverse_list)):
        result.append(reverse_list[max_index - index])

    del reverse_list

    return result


print(reverse(100000))


"""
# 64 bit OS
# Python version: 3.7.0

Line #    Mem usage    Increment   Line Contents
================================================
    13     10.5 MiB     10.5 MiB   @profile
    14                             def reverse(n):
    15     14.4 MiB      3.8 MiB       reverse_list = list(range(n))
    16     14.4 MiB      0.0 MiB       result = list()
    17     14.4 MiB      0.0 MiB       max_index = len(reverse_list) - 1
    18     15.1 MiB      0.0 MiB       for index in range(len(reverse_list)):
    19     15.1 MiB      0.1 MiB           result.append(reverse_list[max_index - index])
    20                             
    21     15.1 MiB      0.0 MiB       del reverse_list
    22                             
    23     15.1 MiB      0.0 MiB       return result
"""
