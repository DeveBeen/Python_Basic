# Chapter03-5
# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용 (JSON)
# 딕셔너리 자료형은 수정과 삭제가 가능하나, 순서가 없고, 키 중복이 존재하지 않는다.

# 선언
a = {'name' : 'Kim', 'phone' : '01033337777', 'birth' : '870514'} # 딕셔너리 선언은 이처럼 '{}'(중괄호)를 사용하여 선언하며 형태는 {'Key' : '값'} 형태로 선언한다. Key는 어떤 자료형이든 될 수 있다.
b = {0 : 'Hello Python'} # 이처럼 Key는 어떤 자료형이든 올 수 있다.
c = {'arr' : [1, 2, 3, 4]} # 값도 '키'만 존재한다면 어떤 자료형이든 올 수 있다.
d = {
    'Name' : 'Niceman',
    'City' : 'Seoul',
    'Age' : 33,
    'Grade' : 'A',
    'Status' : True
} # 이처럼 들여쓰기를 사용하여 딕셔너리 자료형을 선언 할 수도 있다.
e = dict([
    ('Name', 'Niceman'),
    ('City', 'Seoul'),
    ('Age', 33),
    ('Grade', 'A'),
    ('Status', True)
]) # FM방식으로 가독성은 떨어지나 이처럼 dict() 함수를 사용하여 []:리스트 안에 ():튜플 안에 '키'와 '값'을 입력하여 선언도 가능하다.
f = dict(
    Name = 'Niceman',
    City = 'Seoul',
    Age = 33,
    Grade = 'A',
    Status = True
) # 이렇게 선언도 가능하다. 가독성이 훨신 좋으며 오류를 많이 줄일 수 있다.

# 출력
print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f) # 'Key' : 'Value' 형태로 나오며, Class는 dict(사전형)으로 올바르게 출력된다.

print('a - ', a['name']) # dict형에선 인덱싱 할 때는 'Key'입력하여 호출한다. 출력시 그 'Key'에 맞는 'Value'가 출력된다. 만약 'Key'가 존재하지 않을 시 에러가 뜬다 (에러 O)
print('a - ', a.get('name')) # .get() 함수를 사용하여 똑같이 인덱싱이 가능하나, 가장 큰 차이점은 .get() 함수를 사용하면 'Key'가 존재하지 않을 시 'None'이라는 값을 출력한다. (에러 X)
print('a - ', a.get('name1')) # 이처럼 'name1'이라는 'Key'가 존재하지 않아도 오류가 나지 않고 'None'이 출력된다. 매우 안정적이다.
print('b - ', b[0])
print('b - ', b.get(0))
print('f - ', f.get('City'))
print('f - ', f.get('Age'))

# 딕셔너리 추가
a['address'] = 'seoul' # '[]'(대괄호)를 사용하여 괄호 안에는 'Key' 좌변엔 'Value'값을 일력하여 추가 할 수 있다.
print('a - ', a) # 추가한 값이 a dict의 추가되었음을 알 수 있다. (맨 뒤에 붙어 나오는게 X 왜냐하면 dict는 순서가 없기 때문에)
a['rank'] = [1, 2, 3] # 이처럼 추가 할 수 있는 자료형도 자유롭다.
print('a - ', a) # a값에 리스트가 추가됨을 알 수 있다.

# 딕셔너리 길이
print('a - ', len(a))
print('b - ', len(b))
print('c - ', len(c))
print('d - ', len(d)) # len()을 사용하면 Key의 개수가 나온다.

# 딕셔너리 지원 함수 : 주로 반복문을 사용할 때 사용하는 함수가 많다.
# dict_keys, dict_values, dict_items : 반복문(__iter__)에서 사용
print('a - ', a.keys()) # .keys() : dict 안에 'Key'만 출력하여 나열해주는 함수.
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys()) # dict_keys가 뜨면서 'Key'만 가져오는 것을 알 수 있다.

print('a - ', list(a.keys()))
print('b - ', list(b.keys())) # 리스트로 형변환을 하여 'Key'들은 우리가 아는 'List' 형태로 출력이 되었음을 확인 할 수 있다.

print('a - ', a.values()) # .values() : .key()와 반대되는 함수로 이는 'Key'가 아닌 'Value'만 출력한다.
print('b - ', b.values())
print('c - ', c.values()) # dict_values가 뜨면서 'Value'만 가져오는 것을 알 수 있다.

print('a - ', list(a.values()))
print('b - ', list(b.values())) # 위와 같이 똑같은 방법으로 'Value'들을 리스트 형태로 출력함을 알 수 있다.

print('a - ', a.items()) # .items() : 'Key'와 'Value'가 '()'(소괄호)로 묶여 나열해주는 함수.
print('b - ', b.items())
print('c - ', c.items()) # dict_items가 뜨면서 ('Key', 'Value')를 가져오는 것을 알 수 있다.

print('a - ', list(a.items()))
print('b - ', list(b.items())) # 이는 형변환을 해주면 위처럼 리스트로 출력이 되나, 'Key'와 'Value'가 tuple 형태로 묶여 출력됨을 알 수 있다.

print('a - ', a.pop('name')) # .pop() 함수는 인덱싱한 원소를 제거하는 함수였다.
print('a - ', a) # pop을 통하여 'name'인 'Key'와 'Value'가 사라졌음을 알 수 있다.
print('c - ', c.pop('arr'))
print('c - ', c) # pop을 통하여 하나였던 'Key'를 제거하니 빈 dict가 되었음을 알 수 있다.

print('f - ', f.popitem()) # .popitem() : dict안에 임의의 값을 제거한다.
print('f - ', f) # pop에서 지정이 아닌 임의로 값을 삭제한다는 차이점이 있다.

# in 연산자
print('a - ', 'birth' in a) # a dict안에 'birth'가 있는지 문든 연산법이다.
print('b - ', 'city' in d) # in 연산자 : 'Key'를 조회가 가능하다.

# 수정 & 추가
a['test'] = 'test_dict' # 'test'라는 키와 'test_dict'라는 값을 a dict에 추가
print('a - ', a) # 이처럼 원래 dict 내 'test'라는 'Key'가 없으면 값이 추가된다.

a['address'] = 'dj' # 'address'라는 키의 'Value'을 'dj'로 수정
print('a - ', a) # 이처럼 원래 dict 내 'address'라는 'Key'가 이미 존재하면 그에 'Value'가 수정된다.

a.update(birth = '910904') # .update() : 괄호안에 수정 할 값을 선언하여 수정 할 수 있다.
print('a - ', a)

temp = {'address' : 'Busan'}
a.update(temp) # temp라는 또다른 dict를 a dict에 .update()를 통하여 수정 할 수 있다.
print('a - ', a) # 'address'의 'Value'가 temp dict에 'Busan'으로 수정된 것을 알 수 있다.
