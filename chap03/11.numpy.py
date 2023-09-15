import numpy as np

list1, list2 = [1, 2, 3] , [4, 5.0, 6]
a, b = np.array(list1), np.array(list2)
list3 = []

for i, j in zip(list1, list2):
    list3.append(i+j)
print(list3)

list3 = [0, 0, 0]
for i in range(0, 3):
    list3[i] = list1[i] + list2[i]
print(list3)

c = a + b
d = a - b
e = a * b
f = a / b
g = a * 2
h = b + 2

print('a 자료형:', type(a), type(a[0]))
print('b 자료형:', type(b), type(b[0]))
print('c 자료형:', type(c), type(c[0]))
print('g 자료형:', type(g), type(g[0]))
print(c)
print(c, d, e)
print(f, g, h)