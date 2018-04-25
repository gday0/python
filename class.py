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
