"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""

user_num = input('Enter a num: ')  # '6843'

# Using loop:

result = ''
max_index = len(user_num) - 1
for index in range(len(user_num)):
    result += user_num[max_index - index]
print(result)


# Using recursion:


def revers(number, revers_number=''):
    if number:
        revers_number += number[-1]
        return revers(number[:-1], revers_number)
    else:
        return revers_number


print(revers(user_num))