# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).

user_input = input('Enter three numbers (2,-10,15): ')

a = int(user_input.split(',')[0])
b = int(user_input.split(',')[1])
c = int(user_input.split(',')[2])

condition_1 = max(a, b, c)
condition_2 = min(a, b, c)

if a != condition_1 and a != condition_2:
    print(f'avg: {a}')
elif b != condition_1 and b != condition_2:
    print(f'avg: {b}')
elif c != condition_1 and c != condition_2:
    print(f'avg: {c}')
else:
    print('No avg num!')

# List solution:
# user_input = input('Enter three numbers (2,-10,15): ')
# num_list = user_input.split(',')
# print([num for num in num_list if int(num) != max(num_list) and int(num) != min(num_list)][0])
