# 1.	В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

print(len([num for num in range(2, 100) for divider in range(2, 10) if num % divider == 0]))
