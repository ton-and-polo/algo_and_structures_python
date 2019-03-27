"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""
import collections


branches = int(input('Enter quantity of branches: '))
branches_dict = dict()

for i in range(1, branches + 1):
    branch_name = input('Enter branch name: ')
    branch_profit = [int(input(f'Enter {branch_name} profit_{i + 1}: ')) for i in range(4)]

    branches_dict[branch_name] = branch_profit

my_collection = collections.Counter(branches_dict)


avg_profit = int(sum([sum(my_collection[branch]) for branch in my_collection]) / len(my_collection))

above_avg = [branch for branch in my_collection if sum(my_collection[branch]) >= avg_profit]
below_avg = [branch for branch in my_collection if sum(my_collection[branch]) < avg_profit]

print(f'above profit: {above_avg}\nbelow profit: {below_avg}')
