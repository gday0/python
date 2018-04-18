# x = 10

def foo():
    global x
    x = 10
    print(x)

foo()
print(x)
