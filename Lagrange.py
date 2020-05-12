import numpy as np
def phi(i,z):
    p = 1.0
    for j in range(n):
        if i != j:
            p = p * (z - x[j]) / (x[i] - x[j])
    return p

def P(x , y , z):
    s = 0.0
    n = len(x)
    for i in range(n):
        if z == x[i]:
            return y[i]
    for i in range(n):
        s = s + y[i] * phi(i,z)
    return s

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
	x[i] = int(input())
	print('y_',i+1, ':')
	y[i] = int(input())
print('Введи внутренние значения')
for i in range(m):
	print('mid_',i+1,':')
	mid[i] = int(input())

for i in range(m):
    mid_y = P(x, y, mid[i])
print(mid_y)

