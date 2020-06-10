import numpy as np
from math import*
import matplotlib.pyplot as plt
def Index(x, mid_value):
    left = 0
    right = len(x) - 1
    while right - left > 1:
        midle = (right + left) / 2
        midle = floor(midle)
        if x[midle] >= mid_value:
            right = midle
        else:
            left = midle
    return left

def phi(x, y, m):
    n = len(x)
    k = [0.0] * (n - 1)
    b = [0.0] * (n - 1)
    mid_y = np.zeros(m)
    for i in range(n - 1):
        tmp = (y[i + 1] - y[i]) / (x[i + 1] - x[i])
        k[i] = tmp
        b[i] = y[i] - x[i] * tmp
    for i in range(m):
        index = Index(x, mid[i])
        mid_y[i] = k[index] * mid[i] + b[index]

    return mid_y

print('Введите длину вектора x,y:')
n = int(input())
print('Введите длину вектора внутренних значений x:')
m = int(input())

x = np.zeros(n)
y = np.zeros(n)
mid = np.zeros(m)
mid_y = np.zeros(m)
for i in range (n):
	print('x_',i+1,':')
	x[i] = float(input())
	print('y_',i+1, ':')
	y[i] = float(input())
print('Введи внутренние значения')
for i in range(m):
	print('mid_',i+1,':')
	mid[i] = float(input())	
mid_y = phi(x, y, m)

print(mid_y)

x1 = np.concatenate((x,mid), axis=0)
y1 = np.concatenate((y,mid_y), axis=0)

plt.scatter(x1,y1)
plt.plot(mid,mid_y)
plt.show()

