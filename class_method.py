class Person:
    bag = []    # 클래스 속성은 모든 인스턴스에서 공유

    def put_bag(self, stuff):
        Person.bag.append(stuff)

a = Person()
a.put_bag('wallet')

b = Person()
b.put_bag('earphone')

print(a.bag, b.bag)
print(Person.bag)

# 속성 공유하지 않게 하려면
# 인스턴스 속성으로 만들면 된다
class Person1:
    def __init__(self):
        '''인스턴스 만들어질 때 생성'''
        self.bag = []
    # __속성 = 값 # 비공개 클래스 속성

    def put_bag(self, stuff):
        '''인사 메서드'''
        self.bag.append(stuff)

a = Person1()
a.put_bag('wallet')

b = Person1()
b.put_bag('earphone')

print(a.bag)
print(b.bag)

# 정적 메서드
class Calc:
    @staticmethod   # 인스턴스 내용 상관없는 결과값 필요할 때
    def add(a, b):
        print(a+b)

    @staticmethod
    def mul(a, b):
        print(a*b)

Calc.add(3, 35)
Calc.mul(4, 12)
