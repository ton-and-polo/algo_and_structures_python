"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""

# Using loop:

user_num = input('Enter natural number: ')

even_num = []
odd_num = []

# If our number is odd, then its remainder
# of division by two equals one (True).

for num in user_num:
    if int(num) % 2:
        odd_num.append(num)
    else:
        even_num.append(num)

print(f'even: {len(even_num)}, odd: {len(odd_num)}')


# Using recursion:


def odd_even_counter(number, odd=0, even=0):
    # Recursion case:
    if number:
            if int(number[0]) % 2:
                odd += 1
            else:
                even += 1
            return odd_even_counter(number[1:], odd, even)
    else:
        # Base case:
        return f'even: {even}, odd: {odd}'


print(odd_even_counter(user_num))
