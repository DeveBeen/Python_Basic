# Chhapter03-01
# 숫자형

# 파이썬 지원 자료형
"""
int :  정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열 (시퀀스) # 시퀀스는 반복을 처리할 수 있으며 어떤 순서가 있는 데이터 자료형을 말한다.
list : 리스트 (시퀀스)
tuple : 튜플 (시퀀스)
set : 집합
dict : 사전
"""

# 데이터 타입
str1 = "Python"
bool = True
str2 = 'Anaconda'
float_v = 10.0 # float자료형에서 중요한 것은 10.0과 10은 다르다는 것이다. 사람 기준으로 보면 당연히 같은 것이지만, 컴퓨터 입장에서는 수의 크기는 동일하나 자료형은 분명히 다르기 때문에 10 == 10.0은 False이다.
int_v = 7
list = [str1, str2]
dict = {
    "name" : "Machine Learning", # ':' 앞 부분을 Key라고 하며, "Machine Learning"을 꺼내려면 "name"이라는 Key가 필요하다는 사전 형태의 자료형이다.
    "version" : 2.0 # 위와 동일하게 2.0이라는 데이터는 "version"이라는 키가 필요하다.
}
tuple = (7, 8, 9) # 생긴 것은 list랑 똑같이 생겼으나 괄호의 형태가 소괄호이다. (+tuple은 괄호 없이 tuple = 7, 8, 9 라고 선언해도 컴퓨터는 데이터 타입을 tuple로 읽는다.)
set = {3, 5 ,7} # tuple 데이터 타입이랑 헷갈리는 외형이다.

# 데이터 타입 출력
print(type(str1)) # str(문자열)로 잘 출력되었다.
print(type(bool)) # bool(불린) 형태로 잘 출력되었다.
print(type(str2)) # str(문자열)로 잘 출력되었다.
print(type(float_v)) # float(실수형)으로 잘 출력되었다.
print(type(int_v)) # int(정수형)로 잘 출력되었다.
print(type(list)) # list(리스트)로 잘 출력되었다.
print(type(dict)) # dict(사전형)로 잘 출력되었다.
print(type(tuple)) # tuple(튜플)로 잘 출력되었다.
print(type(set)) # set(집합형)으로 잘 출력되었다.

# 숫자형 연산자
"""
+ : 덧셈 연산자
- : 뺄셈 연산자
* : 곱셈 연산자
/ : 나누기 연산자
// : 몫 연산자 ex) 7 // 3 = 2
% : 나머지 연산자 ex) 7 % 3 = 1
abs(x) : x 절댓값 함수 ex) abs(-1) = 1
pow(x, y) : x의 y 제곱 (x ** y랑 똑같다) ex) pow(2,3) = 2 ** 3 = 8
"""

# 정수형
i = 77
i2 = -14
big_int = 7777777777777777777799999999999999999999 # C언어와 달리 Python은 수의 크기만큼 메모리를 할당하므로 모두 정수형 자료를 사용

print(i)
print(i2)
print(big_int)

# 실수형
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9

print(f)
print(f2)
print(f3)
print(f4)

# 연산 실습
i1 = 39
i2 = 939
big_int1 = 7777777777777777777799999999999999999999
big_int2 = 7777787872326781687271641287462764726477
f1 = 1.234
f2 = 3.939

print(">>>> +")
print("i1 + i2 : ", i1 + i2)
print("f1 + f2 : ", f1 + f2)
print("big_int1 + big_int2 : ", big_int1 + big_int2)
# 당연하게 같은 자료형끼리 연산하여 출력하니 같은 자료형으로 나온다.

print(">>>> *")
print("i1 * i2 : ", i1 * i2)
print("f1 * f2 : ", f1 * f2)
print("big_int1 * big_int2 : ", big_int1 * big_int2)
# 당연하게 같은 자료형끼리 연산하여 출력하니 같은 자료형으로 나온다.

# 형 변환
a = 3. # 3.0이랑 같은 의미로 0을 생략을 한 것이다.
b = 6
c = .7 # 위에랑 같은 메커니즘으로 0 생략, 0.7이랑 같은 의미.
d = 12.7

# 타입 출력
print(type(a), type(b), type(c), type(d)) # 당연하게 b만 int(정수형)으로 나오는 것을 알 수 있다.

print(float(b)) # float으로 형변환, int(정수형)이였던, b가 float(실수형)으로 바뀌면서 6이 아닌 6.0이 출력된다.
print(int(c)) # 위와 동일하게 형 변환이 이뤄져 실수형 .7이 정수형 0으로 출력됨을 알 수 있다.
print(int(d)) # 위와 동일하게 형 변환이 이뤄져 실수형 12.7이 정수형 12로 출력됨을 알 수 있다.
print(int(True)) # bool형인 True도 정수형 1로 출력됨을 알 수 있다.
print(float(False)) # bool형 False가 실수형 0.0으로 출력됨을 알 수 있다.
print(complex(3)) # complex(복소수형)으로 정수형 3이 복소수형으로 (3+0j)가 출력됨을 알 수 있다. 복소수형 : (정수부분 + 복소수 * 정수)
print(complex('3')) # 문자형을 숫자형으로 바꿔줌을 알 수 있다. (파이썬 똑똑함)
print(complex(False)) # '0j'가 출력된다.

# 수치 연산 함수
print(abs(-7)) # -7의 절댓값 7이 출력됨.

x, y = divmod(100,8) # 광호 뒤의 수를 나누어 몫과 나머지를 x와 y에 각각 할당해준다.
print(x,y) # x,y에 divmod로 각각 할당했으므로 몫과 나머지가 출력됨을 알 수 있다.

print(pow(5,3), 5 ** 3) # 똑같이 5의 3제곱을 출력한다.

# 외부 모듈
import math # import를 통해 math라는 외부 모듈을 실행

print(math.ceil(5.1)) # 괄호 안의 수보다 크면서 가장 가까운 정수 (가우스 + 1), 여기선 5.1보다 크고 가장 가까운 정수 6이 출력된다.
print(math.pi) # 원주율 출력
