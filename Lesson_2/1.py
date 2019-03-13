"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
"""

# Using loop:

operator = ''

while operator != '0':
    user_input = input('Enter two numbers (5,2): ')

    num_1 = int(user_input.split(',')[0])
    num_2 = int(user_input.split(',')[1])
    operator = input('Enter operator: ')

    while operator == '/' and num_2 == 0:
        num_2 = int(input('You can\'t divide by zero. Enter divider again:\n'))

    if operator == '+':
        print(num_1 + num_2)
    elif operator == '-':
        print(num_1 - num_2)
    elif operator == '*':
        print(num_1 * num_2)
    elif operator == '/':
        print(num_1 / num_2)

    end_program = input('End: yes/no\n')
    if end_program == 'yes':
        operator = '0'
