# Chapter02-2
# 파이썬 완전 기초
# 파이썬 변수

# 기본 선언
n = 700 # n에 좌변 값을 할당한다.

# 출력
print(n) # 변수 n의 할당되어 있는 값을 출력한다.
print(type(n)) # 변수 n의 자료형 type을 출력한다.

# 동시 선언
x = y = z = 700 # Python에서는 이처럼 다변수에 동시 선언이 가능하다.
print(x, y, z)

# 선언
var = 75 # var 라는 변수에 int형 '75'를 선언 후

# 재선언
var = "Change Value" # var 라는 변수에 str(문자열)형 "Change Value"를 다시 선언하면 순차적으로 코드를 읽는 컴퓨터는 가장 마지막에 '덮어씌운' 변수값을 기억한다.

# 출력
print(var) # 출력하면 "Change Value"가 출력됨을 알 수 있다. 이는 '75'로 선언된 var를 "Change Value"로 다시 재선언했으므로 이처럼 출력된다.
print(type(var)) # 위와같이 다시 재선언된 var는 자료형 또한 str(문자열)형으로 변환된 것을 알 수 있다.

# object References
# 변수 값 할당 상태
# 1. Type에 맞는 Object 생성
# 2. 값 생성
# 3. 콘솔 출력

# 예 1)
print(300) # 자료형의 어떠한 언급 없이 값을 입력했다. 이는 내부적으로 작업된 코드이다. (아래 참조)
print(int(300)) # int(정수형)형 자료형을 언급하여 입력했다. 위와 아래는 똑같은 코드인데, 이는 컴퓨터가 내부적으로 Object References 작업을 하였기 때문이다.

# 예 2)
n = 777 # 이 또한 Object References 작업이 내부적으로 된 예시이다. 굳이 정수형을 언급을 안했지만 자동으로 Type에 맞는 Object를 생성하여 값을 집어 넣었다.
print(n, type(n)) # 위에 따라서 변수 n에 대한 Type과 값은 작업이 되었으므로 '777 <class 'int'>'가 출력된다.

m = n # m -> 777 <- n
print(m, n) # m은 777값이 할당되어 있는 n과 같다로 정의 하였으므로, n과 같은 값과 자료형대로 출력이 되는 것을 확인할 수 있다.
print(type(m), type(n))

m = 400 # m -> 400 으로 재선언
print(m, n) # m을 400으로 다시 재선언 하면서, m에는 400이라는 int형 값이 덮어씌워졌으므로 m은 400으로 출력된다.
print(type(m), type(n))

# id(identity)확인 : 객체의 교유값 확인
m = 800 # m에 800이라는 int형 값을 할당
n = 655 # n에 655이라는 int형 값을 할당

print(id(m)) # m에는 800이라는 값이 할당이 되었지만 내부에서 컴퓨터가 작업하기 위해 만든 Object의 id값이 출력값이라는 것
print(id(n)) # 위와 동일한 이야기이다.
print(id(m) == id(n)) # 이는 false로 출력됨을 알 수 있다. 당연히 같은 값이 들어간 것이 아니니 id값 또한 같지 않다.

# 동일 Object 참조
m = 800
n = 800

print(id(m)) # m에는 800이라는 값이 할당이 되었지만 내부에서 컴퓨터가 작업하기 위해 만든 Object의 id값이 출력값이라는 것
print(id(n)) # 위와 동일.
print(id(m) == id(n)) # 이는 true로 출력이 되는데, Python은 어짜피 동일한 값을 가지는 변수라면 하나의 Object로 생성하여 id값을 할당한다. 이로인해 효율적인 작업을 내부적으로 실행함을 알 수 있다.

# 다양한 변수 선언 방법
# 변수 네이밍은 기업과 다른 개발자들이 억량을 판단하는데 간섭하기도 한다.
# Camel Case : numberOfCollegeGraguates 처음 소문자로 시작하여 영어의 각 띄어쓰기마다 대문자로 선언하는 방식 -> 보통 Method를 선언할 시 사용
# Pascal Case : numberOfCollegeGraguates 처음 대문자로 시작하여 영어의 각 띄어쓰기마다 대문자로 선언하는 방식 -> 보통 Class를 선언할 시 사용
# Snake Case : number_of_college_graduates 주로 파이썬에서 변수를 선언할 때 많이 사용
# 강제는 아닌 살짝 국룰 같은 것 하지만 이렇게 쓰는게 기본기가 좋아보인다. (그냥 이렇게 사용하자)

# 허용하는 변수 선언 법 : '_'를 제외한 특수문자가 포함되어 있거나, '숫자'로 시작되는 변수명은 지정할 수 없다.
age = 1 # 소문자로 이뤄진 변수
Age = 2 # 대문자로 시작하는 변수
aGe = 3 # 대문자를 포함한 변수
AGE = 4 # 대문자만 사용한 포함한 변수
a_g_e = 5 # 중간에 '_'가 다수 포함되어 있는 변수
_age = 6 # '_'로 시작하는 변수
age_ = 7 # '_'로 끝나는 변수
_AGE_ = 8 # '_'로 시작하고 끝나면서 가운데 대문자가 1개 이상인 변수

# 예약어는 변수명으로 불가능 : for, as, class 등 Python에서 사용하고 있는 예약어는 사용 불가능하다.
# 예약어는 Google에 'List of Keywords in Python'이라 검색하면 알 수 있다.
