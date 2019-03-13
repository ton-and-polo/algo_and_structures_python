"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""

user_num = input('Enter number: ')
user_digit = input('Enter digit: ')

# Using loop:

result = 0
for num in user_num:
    if num == user_digit:
        result += 1
print(result)


# Using recursion:


def digit_counter(number, digit, result=0):
    if number:
        if number[0] == digit:
            result += 1
        return digit_counter(number[1:], digit, result)
    else:
        return result


print(digit_counter(user_num, user_digit))