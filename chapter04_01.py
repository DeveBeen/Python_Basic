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
