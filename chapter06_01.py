# chapter06-1
# 파이썬 클래스
# OOP(객체 지향 프로그래밍), self, 인스턴스 메소드, 인스턴스 변수

# 클래스 and 인스턴스 차이의 이해가 중요!!
# 클래스와 인스턴스를 붕어빵 기계라 비유했을 떄, class는 붕어빵 틀이면 인스턴스는 그 틀을 찍어내는 요소(객체)라고 생각하면 된다.
# 클래스 변수는 직접 접근이 가능하고 공유하지만, 인스턴스 변수는 객체마다 별도로 존재한다.

# 예제 1
class Dog: # 이처럼 class '이름(object)' 형태로 선언힌다. 모든 class는 object를 상속하기 떄문에 (object)를 선언해도 되고 생략해도 된다.
    # class 속성
    species = 'Firstdog' # Class 변수 : 수 많은 인스턴스 객체들은 모두 자신의 데이터를 가지고 있지만, species라는 것은 동일하기 때문에 클래스 변수는 큰 범위의 개념이다.

    # 초기화 / 인스턴스 속성
    def __init__(self, name ,age): # 객체들을 입력하는 틀을 만든 것
        self.name = name # 이런 각각의 요소가 인스턴스인데, 여러가지 정보를 입력하기 위한 객체를 생성한 것
        self.age = age # 이런 인스턴스 변수는 객체마다 데이터가 별도로 존재한다.

# 클래스 정보
print(Dog) # Class '__main__.Dog'가 출력된다. 붕어빵 틀이 만들어졌다.

# 인스턴스화
a = Dog('mikky', 2)
b = Dog('baby', 3)
c = Dog('baby', 3)
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

print(Dog.species) # 이처럼 직접접근이 가능하다. 이처럼 class로 바로 접근 가능하고,
print(a.species) # 이처럼 인스턴스 변수로도 접근 가능하다.
