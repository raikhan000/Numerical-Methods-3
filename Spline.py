import numpy as np
from math import*
import matplotlib.pyplot as plt
def sweep(a, b, c, f, n):
    alpha = np.zeros(n + 1)
    beta = np.zeros(n + 1)
    x = np.zeros(n)

    for i in range(n):
        d = a[i] * alpha[i] + b[i]
        alpha[i + 1] = -c[i] / d
        beta[i + 1] = (f[i] - a[i] * beta[i]) / d
    x[n - 1] = beta[n]
    for i in range(n - 2, -1, -1):
        x[i] = alpha[i + 1] * x[i + 1] + beta[i + 1]
    return x

def P(x, A, B, C, D, mid_value):
    left = 0
    right = len(x) - 1
    while right - left > 1:
        midle = (right + left) / 2
        midle = floor(midle)
        if x[midle] >= mid_value:
            right = midle
        else:
            left = midle

    index = left
    tmp = mid_value - x[index]
    result = A[index] * (tmp ** 3) + B[index] * (tmp ** 2) + C[index] * tmp + D[index]
    return result
def generateSpline(x, y):
    n = len(x) - 1
    h = (x[n] - x[0]) / n

    a = np.array([0] + [1] * (n - 1) + [0])
    b = np.array([1] + [4] * (n - 1) + [1])
    c = np.array([0] + [1] * (n - 1) + [0])
    f = np.zeros(n + 1)
    for i in range(1, n):
        f[i] = 3 * (y[i - 1] - 2 * y[i] + y[i + 1]) / h ** 2
    s = sweep(a, b, c, f, n + 1)
    A = np.array([0.0] * (n + 1))
    B = np.array([0.0] * (n + 1))
    C = np.array([0.0] * (n + 1))
    D = np.array([0.0] * (n + 1))
    for i in range(n):
        B[i] = s[i]
        A[i] = (B[i + 1] - B[i]) / (3 * h)
        if i != n - 1:
            C[i] = (y[i + 1] - y[i]) / h - (B[i + 1] + 2 * B[i]) * h / 3
        else:
            C[i] = (y[i + 1] - y[i]) / h - (2 * B[i]) * h / 3
        D[i] = y[i]
    return A, B, C, D


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


A, B, C, D = generateSpline(x, y)

for i in range(m):
    mid_y[i] = P(x, A, B, C, D, mid[i])

print(mid_y)

x1 = np.concatenate((x,mid), axis=0)
y1 = np.concatenate((y,mid_y), axis=0)

plt.scatter(x1,y1)
plt.plot(mid,mid_y)
plt.show()
