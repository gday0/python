def calc():
    a = 3
    b = 5
    def mul_add(x):
        return a * x + b
    return mul_add

c = calc()  # c에 저장된 함수가 클로저(closure) # 내부 데이터 숨기고 싶을 때 사용
print(c(1), c(2), c(3), c(4), c(5))

# 연습문제: 호출 횟수 세는 함수
def counter():
    i = 0
    def count():
        nonlocal i
        i += 1
        return i
    return count

c = counter()
for i in range(10):
    print(c(), end=' ')
