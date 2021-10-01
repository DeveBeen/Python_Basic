# chapter06-1
# 파이썬 클래스
# OOP(객체 지향 프로그래밍), self, 인스턴스 메소드, 인스턴스 변수

# 클래스 and 인스턴스 차이의 이해가 중요!!
# 클래스와 인스턴스를 붕어빵 기계라 비유했을 떄, class는 붕어빵 틀이면 인스턴스는 그 틀을 찍어내는 요소(객체)라고 생각하면 된다.
# 클래스 변수는 직접 접근이 가능하고 공유하지만, 인스턴스 변수는 객체마다 별도로 존재한다.

# 예제 1
class Dog1: # 이처럼 class '이름(object)' 형태로 선언힌다. 모든 class는 object를 상속하기 떄문에 (object)를 선언해도 되고 생략해도 된다.
    # class 속성
    species = 'Firstdog' # Class 변수 : 수 많은 인스턴스 객체들은 모두 자신의 데이터를 가지고 있지만, species라는 것은 동일하기 때문에 클래스 변수는 큰 범위의 개념이다.

    # 초기화 / 인스턴스 속성
    def __init__(self, name ,age): # 객체들을 입력하는 틀을 만든 것
        self.name = name # 이런 각각의 요소가 인스턴스인데, 여러가지 정보를 입력하기 위한 객체를 생성한 것
        self.age = age # 이런 인스턴스 변수는 객체마다 데이터가 별도로 존재한다.

# 클래스 정보
print(Dog1) # Class '__main__.Dog'가 출력된다. 붕어빵 틀이 만들어졌다.

# 인스턴스화
a = Dog1('mikky', 2)
b = Dog1('baby', 3)
c = Dog1('baby', 3)
# 이처럼 몇개의 변수든 __init__메소드에서 정의한 매개변수 (name, age) 데이터를 입력할 수 있다.

# 비교
print(a == b, id(a), id(b)) # 이 둘은 id 값이 다르기 때문에 다르다. (당연한 것)
print(b == c, id(b), id(c)) # 만약 값을 완전히 같게 입력해도, 이는 다른 id값을 가지고 물론 다르다 판단을 한다. -> 인스턴스화 시킨 객체는 값이 같아도 변수가 다르면 다 다르다고 판단.

# 네임스페이스 : 객체를 인스턴스화 할 때 자기만의 저장된 공간
print('dog1', a.__dict__) # 이렇게 각각의 속성이 출력됨을 볼 수 있다. (__dict__ : 딕셔너리 속성)
print('dog2', b.__dict__)

# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age)) # 이처럼 각각의 인스턴스를 인덱싱하여 foramt으로 값을 집어넣어 출력할 수 있다.

if a.species == 'Firstdog': # a의 클래스 변수 값은 인스턴스의 상관없이 결국, 'Firstdog'이므로, 이는 T, 실행된다.
    print('{0} is a {1}'.format(a.name, a.species)) # .species를 통하여 클래스 객체 값을 가져오므로, 이는 a의 인스턴스 값과 a의 클래스 값을 출력한다.

print(Dog1.species) # 이처럼 직접접근이 가능하다. 이처럼 class로 바로 접근 가능하고,
print(a.species) # 이처럼 인스턴스 변수로도 접근 가능하다.

# 예제 2
# self의 이해
class SelfTest:
    def func1():
        print('Func1 called')
    def func2(self): # 클래스를 실행 할 때, 선언한 메소드는 __init__메소드가 포함되어야 하는데 이는 파이썬이 내부적으로 실핼해주므로 생략이 가능하다.
        print(id(self)) # 아래 변수 f의 id값과 동일하게 출력된 것을 알 수 있다.
        print('Func2 called')

f = SelfTest() # 클래스라는 도면으로 f라는 객체에 인스턴스화 시킨 것, 이때 f는 SelfTest의 인스턴스이고, 클래스의 객체이다. 관점에 따라 다른 것.

print(dir(f)) # dir(): 사용할 수 있는 메소드를 모두 출력해준다.
print(id(f)) # f의 id값을 출력
# f.func1() # 에러가 생긴다. func1은 호출을 하여도 self라는 매게변수가 없다면, 암묵적으로 이는 클래스 메소드라 한다. 따라서 id값이 넘어가도 func1에서 받지 않으므로 에러가 발생하는 것이다.
f.func2() # 위와는 다르게 func2는 호출해도 오류가 생기지 않는다.
# self는 인스턴스를 요구한다. func2에 slef인자에 변수 f가 넘어간 것, 호출을 하려면 메로리 주소값이 필요한데 이를 클래스 내 함수에 메모리 주소를 주는 역할이 self이다.
SelfTest.func1() # 클래스로 바로 접근을 하면 위처럼 에러가 생기지 않고 바로 호출이 가능하다.
SelfTest.func2(f) # self인자가 이미 있는 함수를 같은 방식으로 호출하면 에러가 생기지만, 이처럼 함수안에 선언한 객체를 집어넣으면 오류가 생기지 않는다.

# 예제 3
# 클래스 변수, 인스턴스 변수
class Warehouse:
    # 클래스 변수
    stock_num = 0 # 재고가 0개

    def __init__(self, name): # 생성자의 역할을 하는 함수이다.
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self): # 소멸자의 역할을 하는 함수이다.
        Warehouse.stock_num -= 1

user1 = Warehouse('Lee')
user2 = Warehouse('Cho') # 두개의 값을 입력하였기 때문에 Warehouse.stock_num은 +1이 두 번 되므로 2가 된다.

print(Warehouse.stock_num)
# Warehouse.stock_num = 50 처럼 중간에 값을 변경할 수도 있다. (그리 좋은 방법은 아니다.)
print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__) # 네임스 페이스엔 분명 stock_num가 존재할텐데 출력이 안되는 이유는 이는 파이썬이 모두가 공유하는 값이므로 굳이 표기하지 않는다.
print('Before', Warehouse.__dict__)
print('>>>', user1.stock_num) # 만약, 이렇게 호출을 하면 2가 출력이 되는데 이는 파이썬이 위에 Warehouse 네임스 페이스에서 찾아온다.

del user1 # class내 __del__함수가 실행된다.
print('After', Warehouse.__dict__) # 이때는 Warehouse에 stock_num가 1로 바뀌는데, 이는 위에서 User1이라는 인스턴스를 삭제했으므로 함수 __del__이 실행됬다.

# 예제 4
class Dog2:
    # class 속성
    species = 'Firstdog'

    # 초기화 / 인스턴스 속성
    def __init__(self, name ,age):
        self.name = name
        self.age = age

    def info(self): # 개의 정보를 출력하는 메소드
        return '{} is {} tears old'.format(self.name, self.age)

    def speak(self, sound): # 개의 짓는 소리를 입출력을 해주는 메소드
        return '{} says {}'.format(self.name, sound)
# 이처럼 많은 메소드를 제작하여, 여러 기능을 class내 만들 수 있다.

# 인스턴스 생성
c = Dog2('july', 4)
d = Dog2('Marry', 10)
# 메소드 호출
print(c.info())
print(d.info())
# 메소드 호출
print(c.speak('wal wal'))
print(d.speak('Mung Mung')) # 이처럼 하나의 클래스를 생성하여 수 많은 메소드를 통해 데이터를 대입할 수 있다.
