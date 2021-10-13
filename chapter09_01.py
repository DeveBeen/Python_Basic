# Chapter09-1
# 파일 읽기 및 쓰기

# 읽기 모드 : r, 쓰기 모드 : w, 추가 모드 : a, 텍스트 모드 : t, 바이너리 모드 : b
# 상대 경로('../, ./'), 절대경로 ('User/wonbinKim/python_basic/')

# 파일 읽기 (Read)
# 예제 1

# 이처럼 절대경로도 가능 f = open('/Users/wonbinkim/python_basic/resource/it_news.txt')
f = open('./resource/it_news.txt', 'r', encoding='UTF-8')

print(dir(f)) # 속성 확인
print(f.encoding) # 인코딩 확인
print(f.name) # 파일 이름
print(f.mode) # 모드 확인
cts = f.read() # read 메소드를 사용하여 바로 읽어올 수 있다.
print(cts)
f.close() # 반드시 close
