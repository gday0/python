a, b = map(int, input().split())

x = {i for i in range(1, a + 1) if a % i == 0}
print(x)
y = {i for i in range(1, b + 1) if b % i == 0}
print(y)

divisor = set.intersection(x, y)

result = 0

if type(divisor) == set:
    result = sum(divisor)

print(result)
