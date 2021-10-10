# Chapter07-1
# 파이썬 예외 처리의 이해
# 예외 종류
# SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError ....
# 문법적으로 예외가 없지만, 코드 실행 프로세스(단계) 발생하는 예외도 중요
# 1. 예외는 반드시 처리
# 2. 로그는 반드시 남긴다. -> 증거가 있어야 범인을 잡 듯, 로그를 보고 에러를 찾기 위해 남긴다.
# 3. 예외는 던져진다.
# 4. 예외 무시


# SyntaxError : 문법 오류
# print('error) -> ''따음표 형식을 지키지 않았을 떄
# print('error')) -> 괄호 수를 맞추지 않았을 때
# if True -> ':'을 붙이지 않았을 때
#    pass

# NameError : 참조가 없을 때 (선언되지 않은 값을 선언하려 할 때)
# a = 10
# b = 15
# print(c) -> 선언되지도 않은 c를 이처럼 선언할 때

# ZeroDivisionError
# print(100/0) -> 연산에서 오류가 나는 에러

# IndexError
# x = [50, 70, 90]
# print(x[1])
# print(x[4]) -> 선언한 인덱스 번호를 초과하거나 존재하지 않은 원소를 인덱싱 할 때, 오류가 남
# 또는 .pop() 연산 시, 인덱스의 범위를 초과하여 사용하였을 때

# KeyError
# dic = {'name' : 'Lee', 'Age' : 41, 'City' : 'Busan'}
# print(dic['hobby']) -> 존재하지 않은 Key로 인덱싱을 할 때 나는 오류이다.
# print(dic.get('hobby')) -> 이처럼 .get() 메소드를 사용하면, 에러가 생기지 않기 때문에 안전한 코딩이 가능하다.

# 예외가 없는 것을 가정하고 프로그램을 작성 -> 런타임 예외 발생 시 예외 처리를 권장 (EAFP)

# AttributeError :  모듈, 클래스에 있는 잘못된 속성 사용 예외
import time
# print(time.time2()) -> 우리가 import한 time모듈엔 time2라는 메소드가 없기 때문에 오류가 뜬다.

# ValueError

# x = [10, 50, 90]
# x.remove(50) -> .remove() : 괄혼안에 값을 제거
# print(x)
# x.remove(200) -> x 안에 200이라는 원소가 없기 때문에 오류가 생긴다.

# FileNotFoundError

# f = open('text.txt') -> text.txt 파일이 프로젝트 내에 없으므로 오류가 발생한다.

# TypeError : 자료형에 맞지 않는 연산을 수행 할 경루
x = [1, 2]
y = (1, 2)
z = 'test'

# print(x + y) -> lifs와 tuple은 합칠 수 없는 연산인 자료형이므로 에러가 안다.
# print(x + z)
# print(y + z)

print(x + list(y)) # 이처럼 연산가능하게 자료형을 변환 시킨 후에 연산을 하여야 에러가 생기지 않는다.

# 예외 처리 기본
# try : 에러가 발생 할 가능성이 있는 코드 실행
# exept 에러명1 : 여러개 가능
# exept 에러명2 : 여러개 가능
# else : try 블록의 에러가 없을 경우 실행
# finally :  항상 마지막에 실행

name = ['Kim', 'Lee', 'Park']

# 예제 1

# try: # if문을 작성하듯 작성하면된다. try 문에는 내가 실행할 (오류가 날 수 있는) 코드를 넣는다. 오류가 없을 시 정상적으로 try문 코드가 실행된다.
#     z = 'Kim' # 만약 여기에 'Cho'와 같은 name 리스트에 없는 원소가 입력되면 ValueError가 생긴다.
#     x = name.index(z)
#     print('Found it! {} in name'.format(z, x+1))
# except ValueError: # if문에 elif처럼 다수의 문을 선언이 가능하다. 현재 이 except문은 ValueError가 났을 때 실행된다.
#     print('Not found it! - Occurred ValueError!')
# else: # 예외가 발생하지 않을 때 실행된다.
#     print('OK! else.')

# 예제 2

# try:
#     z = 'Kim'
#     x = name.index(z)
#     print('Found it! {} in name'.format(z, x+1))
# except Exception: # 이처럼 에러명을 입력하지 않거나 Exception을 입력하면 모든 에러를 잡을 수 있다. -> 단, 어떤 에러가 생긴지 알 수가 없다.
#     print('Not found it! - Occurred ValueError!')
# else:
#     print('OK! else.')

# 예제 3

# try:
#     z = 'cho'
#     x = name.index(z)
#     print('Found it! {} in name'.format(z, x+1))
# except Exception as e: # 이처럼 e를 선언한 후 출력하면, 에러내용을 알 수 있다.
#     print(e)
#     print('Not found it! - Occurred ValueError!')
# else:
#     print('OK! else.')
# finally: # else문은 예외가 발생하지 않았을 때 실행되는 것이지만, finally문은 마지막에 꼭 실행된다.
#     print('OK! finally!')

# 예제 4
# 예외 발생 -> raise 키워드로 예외 직접 발생

try: # 프로그램 설계상 예외를 발생시킬 때, 사용한다.
    a = 'Park'
    if a == 'Kim':
        print('OK! Pass!')
    else:
        raise ValueError # 이렇게 raise 키워드를 사용하여 ValueError를 직접 발생시킬 수 있다.
except ValueError:
    print('Occurred! Exception!')
else:
    print('OK! else!')
