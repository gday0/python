import turtle as t

num = int(input())

t.shape('turtle')
t.color('blue')
t.begin_fill()

for i in range(num):
    t.forward(100)
    t.right(360 / num)

t.end_fill()
