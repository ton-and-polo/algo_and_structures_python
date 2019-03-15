"""
5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""

# Using loop:
max_index = 128
index = 32

while index < max_index:

    row_len = 10  # Initial length of row

    condition = max_index - index
    if index + row_len > max_index:
        row_len = condition  # Assign new row length

    row = ''

    for i in range(row_len):
        row += '{:^{width}}: {}|'.format(index, chr(index), width=len(str(max_index)))
        index += 1

    print(row)

print('End')


# Using recursion:


def print_out_ascii(index, end_index):
    if index >= end_index:
        return 'End'
    else:

        row_len = 10  # Initial length of row

        condition = end_index - index
        if condition < row_len:
            row_len = condition  # Assign new row length

        def my_row(index, row_len, row=''):
            if row_len:
                row += '{:^{width}}: {}|'.format(index, chr(index), width=len(str(end_index)))
                index += 1
                row_len -= 1
                return my_row(index, row_len, row)
            else:
                return row

        print(my_row(index, row_len))

        index += row_len

        return print_out_ascii(index, end_index)


print(print_out_ascii(32, 128))
