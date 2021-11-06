# Chapter09 - 2
# CSV 파일 읽기 및 쓰기

# CSV : NAME - text/csv

import csv # csv 관련 작업을 도와주는 패키지 선언

# 예제 1
with open('./resource/test1.csv', 'r') as f:
    reader = csv.reader(f) # csv 패키지는 reader() 메소드로 파일을 넘겨온다.
    next(reader) # header, 즉 형식을 표기한 해더를 스킵 해준다. (EX) name,code)
    # 객체 확인
    print(reader)
    # 타입 확인
    print(type(reader))
    # 속성 확인
    print(dir(reader)) # __iter__가 있는지 잘 봐볼 것

    for c in reader: # csv 파일을 읽어서 각각 리스트의 형태로 가져온다.
        # print(c)
        # List to srt - 리스트를 문자형으로 변환시키고 싶다.
        print(' : '.join(c)) # .join() 메소드를 사용하여 문자열로 출력 가능 (.앞에 있는게 구분 문자가 된다.)

# 예제 2
with open('./resource/test2.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',') # reader 메소드 매개변수로 delimiter='' 형태를 넣을 수 있는데, ''안에 있는 기호는 구분자이다.
# delimiter = ',' 가 기본값으로 지정되어 있다. print()에 end=\n이 생략되있는 것과 같은 원리이다.
    for c in reader: # 위에서 구분자가 틀리면 csv 파일을 가져올 때, 1가지를 각각의 리스트 형으로 가져온다.
        print(c)

# 예제 3
with open('./resource/test1.csv', 'r') as f:
    reader = csv.DictReader(f) # 딕셔너리 형태로 저장된다.

    print(reader)
    print(type(reader))
    print(dir(reader))

    for c in reader: # {'Name': '', 'Code' : ''}로 저장됨을 알 수 있다.
        for k,v in c.items(): # k,v (key, value) in .items() 메소드로 Key 와 Value를 각각 가져온다.
            print(k,v) # 출력 하면 키와 값이 각각 출력됨을 알 수 있다. KEY VALUE 형태로 출력된다.
        print('-'*10)

# 예제 4
w = [[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18], [19,20,21]]

with open('./resource/write1.csv', 'w', encoding='utf-8') as f:
    print(dir(csv))
    wt = csv.writer(f) # writer() : csv 파일 쓰기 메소드이다.

    # dir과 type 확인 - 습관을 들이는게 중요하다.

    for v in w: # 리스트 내에 있는 리스트를 반복 하므로 리스트 당 한줄 씩 작성된다.
        wt.writerow(v) # writerow() : 한 줄씩 작성

# 예제 5
with open('./resource/write2.csv', 'w', encoding='utf-8') as f:
    # 필드명
    fields = ['One', 'Two', 'Three']

    # Dict Writter
    wt = csv.DictWriter(f, fieldnames=fields)
    # Header Writer
    wt.writeheader() # header 설정

    for v in w:
        wt.writerow({'One':v[0], 'Two':v[1], 'Three':v[2]}) # 위에 작성한 필드 네임이 정확이 맵핑이 되어야 한다.
