"""
7.	По длинам трех отрезков, введенных пользователем, определить возможность
существования треугольника, составленного из этих отрезков. Если такой
треугольник существует, то определить, является ли он
разносторонним, равнобедренным или равносторонним.
"""

a = int(input('Enter length a: '))
b = int(input('Enter length b: '))
c = int(input('Enter length c: '))

if (a + b > c) or (b + c > a) or (c + a > b):
    if a != b and b != c:
        print('abc - miscellaneous triangle')
    elif a == b and b == c:
        print('abc - equilateral triangle')
    elif a == b or b == c or c == a:
        print('abc - isosceles triangle')

else:
    print('abc - not a triangle')
