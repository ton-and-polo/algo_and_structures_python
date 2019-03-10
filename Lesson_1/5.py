# 5.	Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв.

import string

user_input = input('Enter letters (a,z): ')
zero_index = 1

index_1 = (string.ascii_lowercase.index(user_input.split(',')[0].lower())) + zero_index
index_2 = (string.ascii_lowercase.index(user_input.split(',')[1].lower())) + zero_index

if index_1 > index_2:
    letters_between = (index_1 - index_2) - zero_index
elif index_1 < index_2:
    letters_between = (index_2 - index_1) - zero_index
else:
    letters_between = 0

print(f'index_1: {index_1}\nindex_2: {index_2}\nletters_between: {letters_between}')
