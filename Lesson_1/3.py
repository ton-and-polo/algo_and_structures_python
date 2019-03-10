# 3.	По введенным пользователем координатам двух точек вывести
# уравнение прямой вида y = kx + b, проходящей через эти точки.

point_1 = (input('Enter (x1,y1): ')).split(',')  # '-7,-5'
point_2 = (input('Enter (x1,y1): ')).split(',')  # '2,1'

x1 = float(point_1[0])
y1 = float(point_1[1])

x2 = float(point_2[0])
y2 = float(point_2[1])

k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2

if b >= 0:
    print('y={0:.1f}x+{1:.1f}'.format(k, b))
else:
    print('y={0:.1f}x{1:.1f}'.format(k, b))
