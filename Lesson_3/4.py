# 4.	Определить, какое число в массиве встречается чаще всего.
from random import randint
from collections import Counter


my_list = [randint(0, 100) for _ in range(50)]

result_1 = Counter(my_list).most_common(1)
print(f'Frequency using Counter: {result_1[0][1]}')


result_2 = [my_list.count(i) for i in my_list]
print(f'Frequency using count(): {max(result_2)}')
