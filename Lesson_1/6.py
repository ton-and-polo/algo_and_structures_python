# 6.	Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

from string import ascii_lowercase

user_input = int(input('Enter number (1-24): '))
print(ascii_lowercase[user_input - 1])