# Chapter03-2
# 파이썬 문자형

# 문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!''' # 문자열 생성 복습 : 이는 모두 똑같은 문자열이다.

print(type(str1), type(str2), type(str3), type(str4)) # 모두 str(문자열) class로 출려된다.
print(len(str1), len(str2), len(str3), len(str4)) # len함수 : 문자열의 길이를 구한다 '띄워쓰기 포함'

# 빈 문자열
str1_t1 = '' # ''(작은 따옴표) 또는 ""(큰 따옴표)로 선언하면, 빈 문자열 선언이다.
str2_t2 = str() # str()(문자열 자료형 선언)또한 빈 문자열을 선언할 때 쓰인다, (살짝 고급표현)

print(type(str1_t1), len(str1_t1)) # 이와 같이 빈 문자열을 출력하면, Class는 str(문자열)로 나오고, 문자열의 길이는 '0'임을 알 수 있다.
print(type(str2_t2), len(str2_t2)) # 위 아래 둘 다 문자열의 길이가 '0'이 나오는 이유는 우리는 띄어쓰기를 선언한게 아닌 빈 문자열을 선언했기 때문이다.

# 이스케이프 문자 사용
"""
참고 : Escape 코드

\n : Enter(줄바꿈)
\t : Tap(줄간격)
\\ : \(역슬레시) 문자 출력
\', \" : 작은,큰 따옴표 문자 출력
\000 : Null(널)문자 출력
"""
# I'm Boy 와 같은 ' 기호를 출력하고 싶을 때 사용

print("I'm Boy") # 이와 같이 큰 따옴표 안에 묶어주면 정상 출력되지만 괄호 안에 'I'm Boy'를 넣으면 오류가 난다.
print('I\'m Boy') # 만약 긴 텍스트 문서등을 가져와 사용할 떄, 작은 따옴표를 안에 두고 그대로 출력하고 싶다 할 떄, '\'(역슬레시) 기호인 이스케이프 문자를 원하는 특수문자 앞에 붙이면 된다.
print('I\\m Boy') # 물론 '\'기호 조차 출력이 가능하다.
print('a \t b') # '\t'는 키보드의 tap 만큼 거리를 벌려 출력해준다.
print('a \n b') # '\n'은 키보드의 Enter(줄바꿈)을 하여 출력한다.
print('a \"\" b') # 이는 헷갈릴 수 있지만, 그냥 큰 따옴표 2개 앞에 이스케이프 문자를 넣어 오류 없이 출력시키는 용도다.

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1) # ""앞에 escape code 를 넣었으므로, "retro games"가 문자 그대로 출력된다.
escape_str2 = 'What\'s on TV?'
print(escape_str2) # 위와 동일하게 What's 그대로 출력된다.

# 탭, 줄 바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"

print(t_s1) # Escape 문자를 사용한 예시 (TAP)
print(t_s2) # Escape 문자를 사용한 에시 (Enter)

# Raw String 출력 : Escape code를 무시하게 함 '\'(역슬레시)
raw_s1 = r'D:\tpython\test' # 원래는 \t가 Escape 문자로 인식되어 Tap이 출력되어야 한다.
print(raw_s1) # 하지만 raw string 문자를 사용해 '\'가 문자 그대로 인식되어 출력됨을 알 수 있다.
# 운영체제마다 다른 파일 드라이브 주소 등 사용하는 슬레시가 다르기 때문에 Escape 문자를 사용하고 싶지 않을 때 보통 Raw String을 사용한다.

# Multi Line 입력
multi_str = '''
string
Multi Line
test
'''
# 작은 따옴표 3개 또는 큰 따옴표 3개로 긴 텍스를 Multi Line으로 선언이 가능하다.
multi_str = \
'''
string
Multi Line
test
'''
#하지만 전 처럼 선언하면 가독성이 떨어지기 때문데 '\'기호를 사용하여 이처럼 선언 할 수 있다. (파이썬은 \로 끝나면 이 다음에 어떤 변수를 바인딩 하는구나 라고 인식을 한다.)
print(multi_str) # 위처럼 Multi line을 사용하여 긴 텍스트를 변수에 바인딩 할 수 있다.

# 문자열 연산
str_o1 = "python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Deajeon Busan Jinju"

print(str_o1 * 3) # 문자열 * 정수 출력을 하면 그 문자가 정수번 반복 출력된다.
print(str_o1 + str_o2) # 문자열 + 문자열 출력 시 문자열 두개가 이어져서 출력된다.
print('y' in str_o1) # 이는 'y'라는 문자가 str_o1("Python")이라는 문자열 안에 있어? 라는 뜻으로 여기에선 True가 출력됨을 알 수 있다.
print('a' in str_o2) # 위와 같은 실습 : 소문자 'a'와 대문자 'A'는 다르므로 False가 출력된다.
print('P' not in str_o2) # 이는 'p' 문자열은 str_o2("Apple")안에 없지? 라는 뜻으로 여기에선 False가 출력된다.

# 문자열 형 변환
print(str(66), type(str(66))) # 출력을 하면 66이라는 정수가 나와 정수형과 혼동할 수 있지만, 이는 Class 'str'인 문자열이다. (문자:66을 의미)
print(str(10.1), type(str(10.1))) # 이 또한 실수형이 아닌 문자형
print(str(True), type(str(True))) # 이 또한 boolean형이 아닌 문자형이다.

# 문자열 함수 (upper, isalnum, startwith, count, endswith, isalpha...)

print("Capitalize : ", str_o1.capitalize()) # .capitalize() : 첫 글자를 대문자로 바꿔주는 문자열 함수이다.
print("endswith? : ", str_o2.endswith("e")) # .endswith() : 마지막 글자가 괄호 안에 있는 문자랑 같은지를 물어보는 문자열 함수이다.
print("replace : ", str_o1.replace("tho", "Good")) # .replace() : 괄호 안에 있는 전 문자열을 후 문자열로 대체시켜서 출력하는 문자열 함수이다.
print("sorted : ", sorted(str_o1)) # sorted() : 괄호 안에 있는 문자열을 List형으로 출력해주는 문자열 함수이다.(강의에서는 정렬되어 출력됨, 이 기준에 대해서는 List에서 다룰 예정)
print("split : ", str_o4.split(' ')) # .split() : 괄호 안에 있는 문자를 기준으로 각각의 단어로 List형으로 쪼개주어 출력하는 함수이다.

# 반복 (시퀀스)
im_str = "Good Boy!"
print(dir(im_str)) # dir() 출력값에 '__iter__'가 존재하면 이는 반복 할 수 있다는 뜻이다.

for i in im_str: # 반복문 출력이 가능함을 알 수 있다.
    print(i)

# 슬라이싱 : index를 사용해 문자열을 슬라이싱하여 가져오게한다.
str_sl = "Nice Python"

print(len(str_sl)) # 파이썬의 문자열은 이처럼 한 글자마다 순서가 정해지므로, str_sl은 0~10까지 총 11자리가 존재함을 알 수 있다.
print(str_sl[0:3]) # [0:3]은 인덱스(index)를 의미하므로 0,1,2,3 : Nice가 출력이 되는게 아닌 0,1,2: Nic 까지만 출력된다. (a:b 는 a부터 b-1까지 출력이 된다.)
print(str_sl[5:]) # [5:]은 5자리부터 끝까지 가져와라는 의미로 여기에선 "Python"이 모두 출력된다. ([5:] = [5:11])
print(str_sl[:len(str_sl)]) # len(str_sl) = 11 이므로 이는 [:11]과 같은 인덱스이다. 따라서 처음부터 11까지 출력하라는 것이다. ([:11] = [0:11])
print(str_sl[:len(str_sl)-1]) # len을 사용하여 정수형 11을 추출하였고 이는 index안에서 산수를 통해 계산도 가능하다. 따라서 이는 [:10]과 같다.
print(str_sl[1:9:2]) # index [a,b,c]표현은 a에서 b-1까지의 문자열을 가져오되, c칸 만큼씩 띄어서 가져오라는 의미이다. 여기선 "iePt"가 출력된다. (1,3,5,7 출력)
print(str_sl[-5:]) # "-" (마이너스 : 음수) 기호는 음의 순서로 문자열을 거꾸로 -1부터 배정된다. -1은 'n', -2는 'o', -3는 'h' ...
print(str_sl[1:-2]) # 위에서 설명했듯이 -2는 'o'인데 이를 1부터 'o의 자리 -1'까지 출력하라 뜻이 되므로 'ice Pyth'가 출력된다. ([1:-2] = [1:9])
print(str_sl[::2]) # 처음부터 끝까지 2칸 씩 가져와라 라는 뜻
print(str_sl[::-1]) # 우측부터 좌측으로 -1칸 씩 이므로, 문자열이 우측부터 좌측으로 반대로 출력된다.

# 아스키 코드(또는 유니코드)
a = 'z' # 'z'는 파이썬이 컴퓨터에 표기하기 위해 아스키 코드라는 값으로 처리가 되어있다.
# 순서 : 개발자가 문자 입력 > 파이썬이 아스키 코드값으로 변환 > 컴퓨터가 인식 > 코드표에 아스키 코드 값과 일치하는 문자를 출력 > 개발자가 문자 인식
print(ord(a)) # ord() : 괄호 안에 문자의 아스키 코드 값을 출력해준다.
print(chr(122)) # chr() : 괄호 안에 아스키 코드 값을 문자로 출력해준다.
