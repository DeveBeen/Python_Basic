# Chapter04-1
# 파이썬 제어문
# IF 실습

# 기본 형식
print(type(True)) # 0이 아닌 수, "abs"같은 문자, [1, 2, 3...] 데이터가 있는 리스트, (1, 2, 3...) 데이터가 있는 튜플 등등 모두 'True'로 취급 (데이터의 '유')
print(type(False)) # 0, "", [], (), {} 등등 데이터가 '무'인 것은 모두 False로 취급한다.

# 예1

if True: # if문은 'if 조건식'형태로 현재 if문은 True면 'Good'을 출력하라는 if문이다.(if문은 들여쓰기가 매우 중요하다.)
    print('Good')

if False: # False 상태가 아닌 조건문으로 'Bad'가 출력이 되지 않는다.
    print('Bad')

# 예2
if False:
    print('Bad!')
else: # if문이 실행이 되지 않는다면, else문이 실행된다.
    print('Good!')

# 관계 연산자
# >, >=, <, <=, ==, !=
x = 15
y = 10

print(x == y) # x랑 y가 같은지를 출력 -> False
print(x != y) # x랑 y가 다른지를 출력 -> True
print(x > y) # x가 y보다 큰지를 출력 -> True
print(x >= y) # x가 y보다 크거나 같은지를 출력 -> True
print(x < y) # x가 y보다 작은지를 출력 -> False
print(x <= y) # x가 y보다 작거나 같은지를 출력 -> False

# 예3
city = ""
if city: # city는 빈 문자열이므로 'False' 즉, else가 출력된다.
    print("You are in : ", city)
else: # 위 city에 값을 대입하면 'True'값으로 if문이 출력된다.
    print("Please enter your city")

city2 = "Seoul"
if city2: # 값을 넣으면 실행됨을 볼 수 있다.
    print("You are in : ", city2)
else:
    print("Please enter your city")

# 논리연산자(중요)
# and, or, not
a = 75
b = 40
c = 10

print('and : ', a > b and b > c) # a가 b보다 크고, b가 c보다 큰지를 물어보는 '모두' 만족해야하는 논리연산자 : and
print('or : ', a > b or b > c) # a가 b보다 크거나 b가 c보다 큰지를 물어보는 '한가지만' 만족해도 되는 논리연산자 : or
print('not : ', not a > b) # a가 b보다 크다의 결과값의 역을 출력하는 논리연산자 : not

# 산술, 관계, 논리 우선순위
# 우선순위 산술 > 관계 > 논리 순서로 실행
print('e1 : ', 3 + 12 > 7 + 3) # 3+12와 7+3인 산술을 먼저 진행 후 '>' 관계를 물어봤으므로 'True'가 출력
print('e2 : ', 5+ 10 * 3 > 7 + 3 * 20)
print('e3 : ', 5+ 10 > 3 and 7 + 3 == 10) # 산술,관계,논리가 모두 들어있는 경우, 같은 방식으로 산술이 먼저 계산되어 관계연산으로 T or F 가 정해지고, 논리연산자에 의하여 최종적인 값이 출력된다.
print('e4 : ', 5 + 10 > 0 and not 7 + 3 == 10)

# 관계,논리 연산자를 사용한 if문
score1 = 90
score2 = 'A'

if score1 >= 90 and score2 == 'A': # score1은 90 이상이고, score2는 'A'이므로 이는 참으로 if문이 실행된다. 만약 아니라면 else문이 실행된다.
    print('Pass')
else:
    print('Fail')

id1 = 'vip'
id2 = 'admin'
grade = 'platinum'

if id1 == 'vip' or id2 == 'admin': # vip나 admin id를 한가지만 만족해도 if문 출력
    print('관리자 입장')

if id2 == 'admin' and grade == 'platinum':
    print('최상위 관리자')

# 다중조건문
num = 90

if num >= 90:
    print('Grade : A')
elif num >= 80: # if외 다른 추가 조건을 위해 else if를 줄인 elif문을 다중으로 조건문 사용이 가능하다
    print('Grade : B')
elif num >= 70:
    print('Grade : C')
else:
    print('과락')

# 중첩조건문
grade = 'A'
total = 95

if grade == 'A':
    if total >= 90: # if문 안에 이처럼 if문을 넣어 조건이 참인 중에 다른 조건이 참인 케이스를 나눌 수 있다.
        print('장학금 100%')
    elif total >= 80:
        print('장학금 80%')
    else:
        print('장학금 50%')
else:
    print('장학금 없음')

# in, not in

q = [10, 20, 30]
w = {70, 80, 90, 100}
e = {"name" : "Lee", "city" : "Seoul", "grade" : "A"}
r = (10, 12, 14)

print(15 in q) # 15는 q안에 있으므로 'True'
print(12 not in r) # 12는 r에 있지만 not 연산자로 인하여 'False'
print("name" in e) # 딕셔너리 같은 자료형은 in 연산자를 사용할 시에 Key를 조회 할 수 있다.
print("Seoul" in e.values()) # 하지만 이처럼 values() 함수를 사용하면, 값도 조회 가능하다.
