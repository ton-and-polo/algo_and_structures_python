"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""

user_input = input('Enter numbers separated by space (415 760 32 78): ')
numbers_list = user_input.split()

# Using loop:

my_dict = {}
for number in numbers_list:
    my_dict[number] = sum([int(char) for char in number])
result = sorted(my_dict.items())[-1]
print(f'num: {result[0]} sum: {result[1]}')


# Using recursion:


def num_and_max_sum(user_input, my_dict={}):
    if user_input:

        def sum_items(number, sum=0):
            if number:
                sum += int(number[0])
                return sum_items(number[1:], sum)
            else:
                return sum

        my_dict[user_input[0]] = sum_items(user_input[0])
        user_input.remove(user_input[0])
        return num_and_max_sum(user_input, my_dict)
    else:
        result = sorted(my_dict.items())[-1]
        return f'num: {result[0]} sum: {result[1]}'


print(num_and_max_sum(numbers_list))
