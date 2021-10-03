import sys
import inspect
# from ..sub2 import module2

# module1.py
def mod1_test1():
	print ("Module1 -> Test1")
	print("Path : ", inspect.getfile(inspect.currentframe())) # 이 파일이 샐행되는 위치 경로를 출력해준다.

def mod1_test2():
	print ("Module1 -> Test2")
	print("Path : ", inspect.getfile(inspect.currentframe()))
