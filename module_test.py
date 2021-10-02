# 모듈 사용 실습

import sys # 이처럼 import로 모듈을 가져온다.

print(sys) # (built-in)이 출력되는데, 이는 파이썬 내부에 이미 존재하는 모듈이라는 것이다.
print(sys.path) # 우리가 만든 모듈 또는 그 모듈을 모아둔 패키지의 경로, 즉 주소를 출력해주는 메소드이다.

print(type(sys.path)) # 이것의 타입이 리스트로 뜨는 것을 확인 할 수 있다. 즉, 모듈을 추가하려면 append 메소드를 사용하면 된다.

# 모듈 경로 삽입 : append 메소드
#sys.path.append('/User/wonbinKim/Desktop/math') # 이렇게 주소를 입력하여 패키지 등록이 가능하다.

#print(sys.path) # 추가된 것을 알 수 있다.

#import test_module

# 모듈 사용
#print(test_module.power(10,3)) # 우리가 만든 모듈을 이처럼 사용이 가능하다.

import chapter06_02 # 위에서 sys.path로 확인한 주소 내에는 지금 작성하고 있는 python_basic도 존재하므로, 이 파일 내 chapter들은 모듈로 import해올 수 있다.

print(chapter06_02.add(10,1000)) # 이처럼 정상적으로 모듈을 가져온 것을 알 수 있다.
