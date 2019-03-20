"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""
import timeit
import cProfile


def euclidean_1(x, y):
    if x != 0 and y != 0:
        if x > y:
            if x % y == 0:
                return y
            else:
                x = x % y
                return euclidean_1(x, y)
        else:
            if y % x == 0:
                return x
            else:
                y = y % x
                return euclidean_1(x, y)


def euclidean_2(x, y):
    remainder = x % y
    if not remainder:
        return y
    else:
        return euclidean_2(y, remainder)


def main(x, y):
    euclidean_1(x, y)
    euclidean_2(x, y)


print(timeit.timeit('euclidean_1(30, 18)', globals=globals()))
print(timeit.timeit('euclidean_2(30, 18)', globals=globals()))

"""
0.840802995
0.483365697
"""

print(cProfile.run('main(30, 18)'))

"""
         10 function calls (6 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      3/1    0.000    0.000    0.000    0.000 1.py:10(euclidean_1)
      3/1    0.000    0.000    0.000    0.000 1.py:26(euclidean_2)
        1    0.000    0.000    0.000    0.000 1.py:34(main)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
