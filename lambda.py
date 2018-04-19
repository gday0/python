# 함수 선언하여 10씩 더하기
def plus_ten(x):
    return x + 10

print(list(map(plus_ten, [51, 4, 33])))

print(list(map(lambda x: x + 10, [51, 4, 33])))

# 람다 표현식으로 10씩 더하기
f = lambda x: x + 10
print(list(map(f, [51, 4, 33])))

# 람다 표현식 자체를 호출하여 10 더하기
print((lambda x: x + 10)(7))

# !주의! 람다 표현식 안에서는 새 변수를 선언할 수 없음
# 변수가 필요할 경우 def로 함수 만들기
# 람다 표현식 자체로 두 변수 더하기
y = 10
print((lambda x: x + y)(7))

# 짝수(2의 배수)만 문자열 처리
# 람다 표현식에서 if 사용 시 반드시 else 사용. elif는 사용 불가 -> if를 여러번 사용해야
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(map(lambda x: str(x) if x % 2 == 0 else x, a)))

# 리스트에서 홀수는 문자열 변환, 2는 실수로 변환, 나머지는 10 더하기
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda x: str(x) if x % 2 == 1 else float(x) if x == 2 else x + 10, b)))

# 위의 경우 가독성이 떨어지므로 억지로 람다 사용하기 보다는 def로 함수를 만들고 if, elif 사용하자
def f(x):
    if x % 2 == 1:
        return str(x)
    elif x == 2:
        return float(x)
    else:
        return x + 10

c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(f, c)))

# 리스트(딕셔너리, 세트) 표현식 > lambda, map, filter
a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print([i for i in a if i > 5 and i < 10])

# 연습문제: .jpg, .png 파일만 출력
files = ['font', '1.png', '10.jpg', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docx']

print(list(filter(lambda x: x.find('.jpg') != -1 or x.find('.png') != -1, files)))
