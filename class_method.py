class Person:
    bag = []    # 클래스 속성은 모든 인스턴스에서 공유

    def put_bag(self, stuff):
        Person.bag.append(stuff)

a = Person()
a.put_bag('지갑')

b = Person()
b.put_bag('이어폰')

print(a.bag, b.bag)
print(Person.bag)

# 속성 공유하지 않게 하려면
# 인스턴스 속성으로 만들면 된다
class Person1:
    def __init__(self):
        self.bag = []

    def put_bag(self, stuff):
        self.bag.append(stuff)

a = Person1()
a.put_bag('지갑')

b = Person1()
b.put_bag('이어폰')

print(a.bag)
print(b.bag)
