# Chapter03-6
# 집합(Set) 특징
# 집합(Set) 자료형도 딕셔너리 자료형처럼 중복을 허용하지 않고 순서가 존재하지 않는다. 물론 수정과 삭제는 가능하다.

# 선언
a = set() # set(집합)의 빈 집합은 이와같이 선언한다. set을 붙이지 않고 괄호만 사용하면 튜플 자료형이 됨므로 주의하자.
print(a, type(a))
b = set([1, 2, 3, 4, 4, 4]) # set에 원소를 넣는 선언법은 '()'안에 '[]'형태
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate']) # set도 마찬가지로 어떤 자료형이든 들어 갈 수 있다.
e = {'foo', 'bar', 'baz', 'foo', 'qux'} # 딕셔너리처럼 '{}'(중괄호)를 사용할 수도 있는데, 딕셔너리에서 'Key'없이 'Value'만 선언하면 이는 set(집합형)이다.
f = {42, 'foo', (1, 2, 3), 3.14159} # 이처럼 딕셔너리 형태에다 많은 자료형의 집합 원소를 선언 가능하다.

print('a - ', type(a), a, 2 in a) # 이처럼 in 연산자도 사용가능하다.
print('b - ', type(b), b, 2 in b) # 집합은 중복을 허용하지 않음으로 '4'를 여러개 입력했음에도 하나만 출력됬음을 알 수 있다. (오류가 나지 않는다.)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

# 튜플 변환(set -> tuple)
t = tuple(b) # tuple형으로 형변환이 가능하다.
print('t - ', type(t), t) # 형변환이 된 것을 알 수 있다.
print('t - ', t[0], t[1:3]) # 집합에서 튜플로 형변환을 하면, 시퀀스 속성을 가지기 때문에 슬라이싱 및 인덱싱이 가능하다.

# 리스트 변환 (set -> list)
l = list(c)
l2 = list(e) # list형으로 형변환이 가능하다.
print('l - ', l)
print('l2 - ', l2) # list로 변환이 된 것을 알 수 있다.

# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f)) # 이처럼 len함수로 원소의 개수도 알 수 있다.

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print('s1 & s2 :', s1 & s2) # '&': 교집합 표현 기호이다. s1과 s2의 교집합이 출력된다.
print('s1 & s2 :', s1.intersection(s2)) # .intersection() : 위와 같이 교집합이 출력되는 함수이다.

print('s1 | s2 :', s1 | s2) # '|': 합집합 표현 기호이다. s1과 s2의 합집합이 출력된다.
print('s1 | s2 :', s1.union(s2)) # .union() : 위와 같이 합집합이 출력되는 함수이다.

print('s1 - s2 :', s1 - s2) # '-': 차집합 표현 기호이다. s1과 s2의 차집합이 출력된다.
print('s1 - s2 :', s1.difference(s2)) # .difference() : 위와 같이 차집합이 출력되는 함수이다.

# 중복 원소 확인
print('s1 & s2 : ', s1.isdisjoint(s2)) # .isdisjoint() : 중복된 원소가 있으면 False, 없으면 True가 나오는 함수 (교집합의 원소 유,무 판단)

# 부분 집합 확인
print(s1.issubset(s2)) # a.issubset(b) : a가 b의 부분집합인지 확인하는 함수 (T or F로 출력)
print(s1.issuperset(s2)) # a.issuperset(b) : b가 a의 부분집합인지 확인하는 함수 (위와 반대되는 함수)

# 추가 & 제거
s1 = set([1, 2, 3, 4])

s1.add(5) # .add() : 괄호안 값을 추가해주는 method.
print('s1 - ', s1)

s1.remove(2) # .remove() : 괄호안 값을 제거해주는 method. (만약 없는 원소를 삭제하려 하면 'KeyError'가 발생한다)
print('s1 - ', s1)

s1.discard(3) # .discard() : 괄호안 값을 제거해주는 method. (이 함수는 없는 원소를 삭제하려 선언해도 에러가 발생하지 않는다)
print('s1 - ', s1)

s1.clear() # .clear() :  집합의 원소를 모두 제거해주는 method. (이 함수는 리스트에서도 사용이 가능하다.)
print('s - ', s1)
