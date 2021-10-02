# Chapter06-2
# 파이썬 모듈
# Module : 함수, 변수, 클래스 등 파이썬 구성 요소 등을 모아놓은 파일 (기능 등을 재사용할 때 사용 : import)

def add(x, y): # add function : 덧셈함수
    return x + y

def subtract(x, y): # subtract function : 뺄셈 함수
    return x - y

def multiply(x, y): # multiply function : 곱셈 함수
    return x * y

def devide(x, y): # devide function : 나눗셈 함수
    return x / y

def power(x, y): # power function : 제곱 함수
    return x ** y

# __name__ 사용 : 자체적으로 구동 확인을 위한 테스트 코드가 외부에서 import가 되었을 때, 출력되지 않게 방지해주는 if문이다.
if __name__ == "__main__": # 내가 실행한 파일이 __main__에서 실행되지 않으면 실행하지 않는다. 즉, 외부에서 실행했을 시 __name__은 그 외부의 파일명이므로 자체적인 __main__이 아니므로 외부에서 사용이 가능하다.
    print('-' * 15)
    print('called! __main__')
    print(add(5,5))
    print(subtract(15,5))
    print(multiply(5,5))
    print(devide(10,2))
    print(power(5,3))
    print('-' * 15)
