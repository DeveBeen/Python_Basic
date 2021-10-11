# Chapter08-2
# 파이썬 외장(External) 함수
# 실제 프로그램 개발 중 자주 사용
# 종류 : sys, pickle, shutil, temfile, time, random 등

# 예제 1
import sys
print(sys.argv) # 인자값을 모두 가져오는 함수 -> 쉽게 말해서 파일 주소 불러온다.

# 예제 2 (강제종료)
# sys.exit() -> 프로그램을 강제종료 시키는 함수이다.

# 예제 3 (파이썬 패키지 위치)
print(sys.path) # 모든 패키지들의 위치를 불러온다.

# pickle : 객체 파일 읽기, 쓰기
import pickle # 파이썬에서 지정된 어떠한 데이터 타입(객체)를 저장장치에 쓰고 읽을 때, 사용하는 외장함수이다.

# 예제 4 (쓰기)
f = open('test.obj', 'wb') # ('파일명 또는 파일주소','쓰다(write)+바인더리(bindery) 형이므로 wb')
obj = {1:'python', 2:'study', 3:'basic'}
pickle.dump(obj, f) # 이를 실행하면 obj 확장자 파일이 하나 생성되는데, 그곳에 우리가 할당한 변수 f에 들어있는 딕셔너리가 바인더리 형태로 저장된 것을 볼 수 있다.
f.close() # 언제나 open을 하면 닫아줘야한다.

# 예제 5 (읽기)
f = open('test.obj', 'rb') # 이때는 할당하는 것이 아닌 불러오는 것이므로, 파일에 f가 있어야 한다. ('파일명 또는 파일주소', '읽다(read)+바인더리(bindery) 형이므로 'rb')
data = pickle.load(f) # 쓸때는 dump 읽을땐, load
print(data, type(data))
f.close() # 냉장고 문을 열면 닫자, 실행시키면 딕셔너리형으로 다시 가져왔음을 알 수 있다.

# os : 환경 변수, 디렉토리(파일) 처리 관련, 운영체제 작업 관련 -> os에서 지원하는 작업들 (게임 실행, 폴더 만들기 등)을 파이썬 코드로 사용할 수 있게 하는 함수
# mkdir(폴더 생성), rmdir(폴더 삭제) -> (비어있으면 삭제, 내용이 있으면 삭제되지 않음), rename

# 예제 6
import os
print(os.environ) # 내 컴퓨터에 대한 운영체제 내용을 나오는 함수 (딕셔너리 형태)
print(os.environ['USER']) # 운영체제 정보는 딕셔너리형이므로 키를 사용하여 인덱싱을 통해 value를 가져올 수 있다.
print(os.environ['ATOM_HOME'])

# 예제 7
print(os.getcwd()) # 현재 경로를 표기해주는 함수

# time : 시간 관련 처리
import time

# 예제 8
print(time.time()) # 현재 시간을 가져오는 함수

# 예제 9 (형태 변환)
print(time.localtime(time.time())) # 현재 시간을 년,월,일...으로 분해하여 출력해준다.

# 예제 10 (간단표현)
print(time.ctime())

# 예제 11 (형식표현)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))) # 이렇게 우리가 원하는 표기법을 사용하는 함수도 존재한다.

# 예제 12 (시간 간격 발생)
# for i in range(5):
#     print(i)
#     time.sleep(1) # ()괄호안에 입력한 수의 초마다 (여기선 1초)마다 반복문을 실행하는 함수이다.

# random : 난수 리턴
import random

# 예제 13
print(random.random()) # 0 ~ 1 실수를 랜덤으로 가져오는 함수

# 예제 14
print(random.randint(1, 45)) # 괄호안에 범위 내에 있는 int형 정수를 랜덤으로 가져온다.
print(random.randrange(1,45)) # 이는 range이므로 1~(45-1=44)내에 int형 정수를 가져온다.

# 예제 15 (섞기)
d = [1,2,3,4,5]
random.shuffle(d) # 값을 랜덤으로 재배치하는 함수
print(d)

# 예제 16 (무작위 선택)
c = random.choice(d) # d내에 있는 원소 중 하나를 랜덤으로 가져온다.
print(c)

# webbrowser : 본인 os의 웹 브라우저를 실행
import webbrowser

# webbrowser.open('http://google.com') # 입력한 주소로 방문하게 된다.
# webbrowser.open_new('http://google.com') # 위와 같지만 차이점은 새탭으로 따로 방문한다.
