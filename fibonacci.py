def fib(arg):
    if n < 10 or n > 30:
        return False
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n) + fib(n-1)

n = int(input())
print(fib(n))
