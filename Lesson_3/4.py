# 4.	Определить, какое число в массиве встречается чаще всего.
from random import randint
from collections import Counter


my_list = [randint(0, 100) for _ in range(50)]
result = Counter(my_list).most_common(1)
print(f'num: {result[0][0]}\nfrequency: {result[0][1]}')
