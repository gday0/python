# 빈 클래스
class Person0:
    pass

# method in method
class Person1:
    def greeting(self):
        print('Hello')

    def hello(self):
        self.greeting()

gday = Person1()
gday.hello()

# 특정 클래스의 인스턴스인지 확인
print(isinstance(gday, Person0))
print(isinstance(gday, Person1))

# 클래스 속성
class Person2:
    def __init__(self, name, age, address):
        self.hello = '하이요'
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print('{0} 저는 {1}입니다.'.format(self.hello, self.name))

gday = Person2('죵', 27, '일산')
gday.greeting()

print('이름:', gday.name)
print('나이:', gday.age)
print('주소:', gday.address)

print(type(gday))

# 인스턴스 생성한 뒤 속성 추가하면
# 클래스에는 속성이 추가되지 않고 해당인스턴스에만 생성
gday.mobile = '010-0000-0000'
print(gday.mobile)

# __slots__ 는 다른 속성 생성을 제한하는 용도
class Person:
    __slots__ = ['name', 'age']

con = Person()
con.name = '콘'
con.age = 2
# con.address = '카카오'

# 변수명 앞에 __ 사용하여 비공개 속성 사용
# 비공개 속성은 클래스 안의 메서드에서만 접근 가능
class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet

    def pay(self, amount):
        self.__wallet -= amount
        print('{0}원 남았다.'.format(self.__wallet))

con = Person('콘', 2, '카카오', 10000)
con.pay(2300)

# 비공개 메서드는 클래스 안에서만 호출 가능
class Person1:
    def __greeting(self):
        print('앙뇽')

    def hello(self):
        self.__greeting()

con = Person1()
con.hello()

# 연습문제
class Knight:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def slash(self):
        print('베버리기')

x = Knight(health = 1000, mana = 200, armor = 40)
print(x.health, x.mana, x.armor)
x.slash()
