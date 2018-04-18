start, end = map(int, input().split())

value = [2 ** i for i in range(start, end + 1)]

value.pop(1)
value.pop(-2)

print(value)
