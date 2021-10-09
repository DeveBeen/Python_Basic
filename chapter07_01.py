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
