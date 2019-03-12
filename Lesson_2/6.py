"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""
from random import randint

# Using loop:

# Game conditions:
max_try = 10
answer = randint(0, 100)

for i in range(1, 11):
    user_answer = int(input('Guess num (0-100): '))
    if user_answer == answer:
        print('You win!')
        break
    elif i == max_try:
        print(f'You louse! Correct answer: {answer}')

    else:
        if user_answer > answer:
            print(f'{user_answer} > answer')
        elif user_answer < answer:
            print(f'{user_answer} < answer')


# Using recursion:


def guess_game(answer=randint(0, 100), user_try=1):
    user_answer = int(input('Guess num (0-100): '))

    if user_answer == answer:
        return 'You win!'
    elif user_try == 10:
        return f'You louse! Correct answer: {answer}'
    else:
        if user_answer > answer:
            print(f'{user_answer} > answer')
        elif user_answer < answer:
            print(f'{user_answer} < answer')

        user_try += 1

        return guess_game(answer, user_try)


print(guess_game())