a = list(range(0,10,1))
print(a)

b = tuple(range(3, 10))
print(b)

c = [1, 2, 3]
d = c
print('d is c', d is c)
e = c.copy()
print('e is c', e is c)

for i, v in enumerate(c):
    print('list \'c\'', i, v)
