# Chapter09-1
# 파일 읽기 및 쓰기

# 읽기 모드 : r, 쓰기 모드 : w, 추가 모드 : a, 텍스트 모드 : t, 바이너리 모드 : b
# 상대 경로('../, ./'), 절대경로 ('User/wonbinKim/python_basic/')

# 파일 읽기 (Read)
# 예제 1

# 이처럼 절대경로도 가능 f = open('/Users/wonbinkim/python_basic/resource/it_news.txt')
f = open('./resource/it_news.txt', 'r', encoding='UTF-8') # open('경로', '형태', 'encoding')

print(dir(f)) # 속성 확인
print(f.encoding) # 인코딩 확인
print(f.name) # 파일 이름
print(f.mode) # 모드 확인
cts = f.read() # read 메소드를 사용하여 바로 읽어올 수 있다.
print(cts)
f.close() # 반드시 close

# 예제 2
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f: # 위와 똑같은 형식이지만 close를 사용할 필요없고, 한 번 지정한 파일을 들여쓰기 내로 계속 사용 가능하다.
    c = f.read()
    print(c)
    print(iter(c))
    print(list(c))

# 예제 3
# read() : 전체 읽기, read(10) : 10Byte -> read 안에 숫자를 넣어주면 그에따른 바이트 만큼 가져온다.

with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read(20)
    print(c) # read에 20을 지정하였으므로 20byte만큼만 가져옴을 알 수 있다.
    c = f.read(20)
    print(c) # 위에서 마지막으로 읽었던 마지막을 기준으로 20Byte를 가져온다. (커서가 존재한다.)
    f.seek(0,0) # .seek() : 지정한 위치로 커서를 초기화하는 메소드이다.
    c = f.read(20)
    print(c) #위에서 0,0으로 초기화 하여 다시 처음부터 출력됨을 알 수 있다.

# 예제 4
# readline : 한줄씩 읽어오는 함수 (줄바꿈을 기준으로 읽어온다.)

with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    line = f.readline()
    print(line)
    line = f.readline()
    print(line) # 이또한 커서가 존재하므로 다음 라인이 출력

# 예제 5
# readlines : 전체를 읽은 후 라인 단위 리스트로 저장하는 함수이다.

with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    cts = f.readlines()
    print(cts) # 리스트에 줄 단위로 저장되어 있음을 볼 수 있다.
    print()
    for c in cts:
        print(c, end = '') # 원문이 그래도 나옴을 알 수 있다.

# 파일 쓰기 (Write)

# 예제 1
with open('./resource/contents1.txt', 'w') as f:
    f.write('I love python\n') # .write() : 쓰기 메소드

# 예제 2
with open('./resource/contents1.txt', 'a') as f: # 같은 w 속성으로 쓰기 메소드를 하면 기존의 내용은 지워지고 수정이 된다.
    f.write('I love python2\n') # 하지만 'a(append)'속성으로 쓰기 메소드를 사용하면, 말그대로 내용이 추가가 된다.

# 예제 3
# writelines : 리스트로 되어 있는 것을 파일로 쓸 수 있게하는 매소드
with open('./resource/contents2.txt', 'w') as f:
    list = ['Orange\n', 'Apple\n', 'Banana\n', 'Melon\n']
    f.writelines(list)

# 예제 4
with open('./resource/contents3.txt', 'w') as f:
    print('Test Text Write!', file = f)
    print('Test Text Write!', file = f)
    print('Test Text Write!', file = f) # 프린트문이 여기서 실행되지 않고 지정경로로 open한 파일에서 쓰여졌다.
