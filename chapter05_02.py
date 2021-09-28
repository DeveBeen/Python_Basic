# Chapter05-2
# 파이썬 사용자 입력
# Input 사용법
# 기본 타입(str)

# 예제 1
name = input("Enter your name : ") # 변수 선언 시 input('출력메세지') 함수를 사용하여 선언
grade = input('Enter your Grade : ')
company = input('Enter your Company name : ')

print(name, grade, company) # 바로 출력을 하면 아무 일도 일어나지 않는다. Terminal을 사용하여, 실행 시 출력이된다. cd를 통하여 파일로 이동 후 .py 확장자 실행 (명령어 python [파일명])

# 예제 2
number = input('Enter number : ')
name = input('Enter name : ')

print('type of number', type(number)) # 숫자를 입력하더라도 input()의 기본 타입은 str(문자형)이기 때문에 class가 str로 출력된다.
print('type of name', type(name))

# 예제 3 (계산)
first_number = int(input('Enter first_number : ')) # 이처럼 input 함수 밖에 자료형 함수를 씌워 변수의 자료형을 설정하여 선언한다.
second_nuumber = int(input('Enter second_nuumber : '))

total = first_number + second_nuumber # 선언된 문자는 계산식으로 연산이 가능하다.
print('first_number + second_nuumber : ', total) # 변수들이 정상적으로 정수형을 받은 걸 알 수 있다.

# 예제 4
float_number = float(input('Enter a float_number : '))

print('input float : ', float_number)
print('input type : ', type(float_number)) # 정상적으로 자료형이 변환되어 값이 출력된 것을 알 수 있다.

# 예제 5
print('FirstName - {0}, LastName - {1}'.format(input('Enter First Name : '), input('Enter Second Name : '))) # format을 사용하여 {0}{1}로 할당 순서를 결정 후 출력 한 경우로 input은 print함수 내에서도 선언이 가능하다.(변수를 사용안하고 넣은 케이스이다.)
