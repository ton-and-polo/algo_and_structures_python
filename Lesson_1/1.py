# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

three_digit_num = int(input('Enter three digit number: '))

digit_3 = (three_digit_num % 1000) // 100  # operation in parentheses is redundant, but represents a pattern
digit_2 = (three_digit_num % 100) // 10
digit_1 = (three_digit_num % 10) // 1

addition = digit_1 + + digit_2 + digit_3
multiplication = digit_1 * digit_2 * digit_3

print(f'sum: {addition}\nmult: {multiplication}')

# List solution:
#
# import numpy
#
# user_input = input('Enter three digit number: ')
#
# addition = sum([int(char) for char in user_input])
# multiplication = numpy.prod([int(char) for char in user_input])
#
# print(f'sum: {addition}\nmult: {multiplication}')
