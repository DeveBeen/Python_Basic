# Chapter08-1
# 파이썬 내장 (Built-in) 함수
# 자주 사용하는 함수 위주로 실습
# 사용하다보면 자연스럽게 숙달

# 절댓값을 구해주는 함수 : abs()
print(abs(-3))

# iterable 요소를 검사해주는 함수(참,거짓) : all(), any()
print(all([1, 2, 3])) # 리스트 내 모든 요소가 참이여야 True가 나온다. -> And 조건
print(any([1, 2, 3])) # 리스트 내 요소중에서 하나라도 참이라면 True이다. -> or 조건


# 아스키 코드 변환 함수 : chr() : 아스키 -> 문자 , ord() : 문자 -> 아스키
print(chr(67))
print(ord('C'))

# Index + Iterable 객체를 생성해주는 함수 : enumerate()
for i, name in enumerate(['abc', 'bcd', 'efg']):
    print(i, name) # 리스트를 인덱싱하여 가져올 수 있는 함수이다.

# 반복가능한 객체 요소를 지정한 함수 조건에 맞는 값만 추출하는 함수 : filter()
def conv_pos(x):
    return abs(x) > 2 # 절댓값 x가 2보다 크면 반환한다.

print(list(filter(conv_pos, [1, -3, 2, 0, -5, 6]))) # 이처럼 filter함수를 사용하면 조건내 만족하는 값을 오브젝트로 가져오는데 이를 우리가 원하는 형으로 변환해서 사용할 수 있다.
print(list(filter(lambda x: abs(x) > 2, [1, -3, 2, 0, -5, 6]))) # 위 처럼 함수를 선언 안하고, lambda를 사용하여 이처럼 바꿀 수 있다. 한 번 사용하는용이면 훨신 유연한 코드이다.

# 객체의 주소값(레퍼런스)를 반환해주는 함수 : id()
print(id(int(5)))
print(id(4))

# 요소의 길이를 반환해주는 함수 : len()
print(len('abcdefg'))
print(len([1,2,3,4,5,6,7]))

# 최댓값과 최솟값을 구해주는 함수 : max(), min()
print(max([1,2,3]))
print(max('python study'))
print(min([1,2,3]))
print(min('python study')) # 띄어쓰기가 있으므로 공백이 가장 작은값으로 출력

# 반복가능한 객체 요소를 지정한 함수 실행 후 추출
def conv_abs(x):
    return abs(x)

print(list(map(conv_abs, [1,-3,2,0,-5,6]))) # filter는 조건에 맞게 걸러주는 역이라면 map은 조건에 맞는 모든 요소를 추출해준다.
print(list(map(lambda x:abs(x), [1,-3,2,0,-5,6])))

# 제곱값을 반환해주는 함수 : pow()
print(pow(2,10))

# 반복가능한 객체(Iterable)를 반환해주는 함수 : range()
print(range(1,10,2))
print(list(range(1,10,2)))
print(list(range(0,-15,-1)))

# 반올림 해주는 함수 : round()
print(round(6.5781, 2)) # round(숫자, 소수점 아래 몇번쟤) -> 6.5781을 소수점 아래 2번째에서 반올림을 받았음으로 6.58이 출력된다.
print(round(5.6)) # 뒷 인자가 없으므로 그냥 첫번째자리에서 반올림한다.

# 반복 가능한 객체(Iterable)를 정렬해주는 함수 : sorted()
print(sorted([6,7,4,3,1,2]))
print(sorted(['p','y','t','h','o','n'])) # 알파벳 순서로 정렬해준다.

# 반복 가능한 객체(Iterable)를 더해서 반환해주는 함수 : sum()
print(sum([6,7,8,9,10]))
print(sum(range(1,101)))

# 자료형을 확인해주는 함수 : type()
print(type(3))
print(type({}))
print(type(()))
print(type([]))

# 반복 가능한 객체(Iterable)의 요소를 묶어서 반환해주는 함수 : zip()
print(list(zip([10,20,30], [40,50,60]))) # 원소의 인덱스 번호끼리 튜플형으로 묶어준다.
print(list(zip([10,20,30], [40,50]))) # 만약, 이처럼 len이 다를 경우엔 인덱스 번호가 일치하는 것만 출력한다.
