# Chapter04-2
# 파이썬 반복문
# For 실습

# 코딩의 핵심
# for in <collection>
#   <Loop body>

for v1 in range(10): # for 'for문에서 사용할 변수(C언어에 int i = 0과 비슷)' in range(N-1) : 0 ~ 9
    print('v1 is : ', v1)

for v2 in range(1, 11): # (a, b)는 a부터 b-1까지 변수 v2에 값이 들어간다. : 1 ~ 10
    print('v2 is : ', v2)

for v3 in range(1, 11, 2): # (a, b, c)는 a부터 b-1까지 변수 v3에 대입하되, c칸씩 띄워서 대입. : 1, 3, 5, 7, 9
    print('v3 is : ', v3) # 짝수, 홀수 문제를 제작할 시 다른 언어보다 빠른 코딩이 가능하다.

# 1 ~ 1000 합
sum1 = 0

for v in range(1, 1001): # 1부터 1000까지 수를 모두 더하는 for문.
    sum1 += v # sum = sum + v의 축약어
print('1 ~ 1000 Sum : ', sum1)

print('1 ~ 1000 Sum : ', sum(range(1,1001))) # sum 함수를 통해 간단한 시그마 공식은 해결 할 수 있다.
print('1 ~ 1000 4의 배수의 합 : ', sum(range(4,1001,4)))

# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
# Iterables 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예제 1
names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']

for name in names: # 선언한 리스트의 각 원소를 출력해준다.
    print('You are : ', name)

# 예제 2
lotto_numbers = [11, 19, 21, 28, 36, 37]

for n in lotto_numbers:
    print("Currnet number : ", n)

# 예제 3
word = "Beautiful"

for s in word: # 시퀸스 성질에 의하여 각각 한글자씩 출력되는 것을 알 수 있다.
    print('Word : ', s)

# 예제 4
my_info = {
    'name' : 'Lee',
    'Age' : 33,
    'City' : 'Seoul'
}

for k in my_info:
    print('key : ', k) # 딕셔너리 같은 경우는 이와 같이 key를 가져오는데
for k1 in my_info:
    print('Value : ', my_info[k1]) # 이처럼 리스트의 key값을 넣어줘 'Value'를 꺼내올 수도 있다. (.get(k1) 함수를 사용할 수도 있다.)
for v in my_info.values():
    print('value : ', v) # 위와 같은 방식도 있으나 이처럼 values 함수를 사용하여 'value'를 꺼내올 수도 있다.

# 예제 5
name = 'FineAppLE'

for n in name:
    if n.isupper(): # .isupper() : .앞에 변수의 값이 대문자인지 판별하는 함수. (소문자는 .islowers())
        print(n)
    else:
        print(n.upper()) # .upper() : .앞의 변수의 값을 대문자로 출력해주는 함수.

# break : 불필요하게 반복하는 것을 방지하기 위해 for문 탈출 선언문.
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 17:
        print('Found : 17!')
        break # 이처럼 break를 선언하므로 이 for문 반복문에서 빠져나간다.
    else:
        print('Not found : ', num)

# continue : 어떤 조건을 검사하는 문에서 다시 조건을 검사하는 부분으로 이동시키는 선언문.
lt = ['1', 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is bool: # 자료형을 대조할 땐, 이처럼 'is'를 사용한다.
        continue
    print('current type : ', v, type(v)) # continue문으로 만약 bool형을 만날 시 다시 조건으로 올라가므로, 'True'값이 스킵된다.
    print('multiply by 2', v * 3)
