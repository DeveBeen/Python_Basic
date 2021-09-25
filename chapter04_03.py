# Chapter04-3
# 파이썬 반복문
# while 실습

# while <expr>:
#   <statment(s)>

# 예제 1
n = 5

while n > 0: # while 문 형태는 이와같다. while문은 조건을 만족 할 때까지 계속 반복한다.(무한반복이 많기 때문에 조심해야 한다.)
    print(n)
    n = n - 1

# 예제 2
a = ['foo', 'bar', 'baz']

while a: # 이런 리스트 조건은 T인지 F인지 확실하게 판단하여 무한반복을 생각해야한다.
    print(a.pop()) # 이처럼 pop을 사용하여 리스트 안 원소를 한개 씩 꺼내서 출력하면, 조건문이 f인 순간이 생긴다.

# if 중첩
# 예제 3
# break, continue
n = 5

while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop Ended.')

# 예제 4
m = 5

while m > 0:
    m -= 1
    if m == 2:
        continue
    print(m)
print('Loop Ended.')

# 예제 5
i = 1

while i <= 10:
    print('i : ', i)
    if i == 6:
        break
    i += 1

# while - else 구문

# 예제 6
n = 10

while n > 0:
    n -= 1
    print(n)
    if n == 5:
        break # for문 처럼 이런 break문을 만나지 않는다면, else문이 실행되지 않는다.
else:
    print('else out.')

# 예제 7
a = ['foo', 'bar', 'baz', 'qux']
s = 'qux'
i = 0

while i < len(a):
    if a[i] == s:
        break
    i += 1 # i값을 증가시켜 len 함수로 리스트를 탐색해 볼 수도 있다.
else:
    print(s, 'not found in list')

# 무한반복
#while True:
#    print('Foo')

# 예제 8
a = ['foo', 'bar', 'baz']

while True:
    if not a: # not이므로 False가 되어야 break이다. 따라서 리스트가 비어야 무한반복이 실행되지 않는다.
        break
    print(a.pop())
