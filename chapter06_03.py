# Chapter06-3
# 파이썬 패키지
# 패키지 : 모듈이 뭉쳐있는 폴더
# 패키지 작성 및 사용법
# 파이썬은 패키지로 분할 된 개별적인 모듈로 구성
# __init__.py : python 3.3 부터는 없어도 패키지로 인식 -> 단, 하위 호환을 위해 작성 추천!!
# 파이썬에게 이것이 패키지라고 인식을 시키기 위해 비어있는 init파일을 sub 패키지 내 __init__처럼 작성해야 한다.
# 상대경로 : ..(부모 디렉토리), . (현재 디렉토리) -> 모듈 내부에서만 사용

# 예제 1
import sub.sub1.module1 # .(상대 디렉토리 기호)을 통해서 파일경로를 설명하여 모듈을 가져올 수 있다.
import sub.sub2.module2

# 사용
sub.sub1.module1.mod1_test1()
sub.sub1.module1.mod1_test2()

sub.sub2.module2.mod2_test1()
sub.sub2.module2.mod2_test2() # 모듈에서 호출 해올 수 있다.

print()
print('-' * 30) # 줄바꿈용
print()

# 예제 2
# 위처럼 import를 사용할 때, 패키지안에 모듈을 상대경로를 통해 길게 작성하고, 사용할 때마다 이를 입력해야 한다.
from sub.sub1 import module1
from sub.sub2 import module2 as m2 # 별명을 부여 할 수 있다. (alias)

module1.mod1_test1()
module1.mod1_test2() # 예제 1 이랑은 다르게 from절을 사용하면, 이처럼 간단한 호출명으로 호출이 가능하다.

m2.mod2_test1()
m2.mod2_test2() # 이처럼 또, from절에서 호출명을 지정하여 호출도 가능하다.

print()
print('-' * 30) # 줄바꿈용
print()

# 예제 3
from sub.sub1 import * # '*' 지정한 패키지 내 모든 모듈을 가져오는 기호이다. 왠만하면 사용하지 않는게 좋다, 필요없는 모듈을 굳이 가져와 불필요한 작업도 실행된다.
from sub.sub2 import *

module1.mod1_test1()
module1.mod1_test2()

module2.mod2_test1()
module2.mod2_test2() # 이처럼 모든 모듈을 from 사용하여 가져왔기 때문에, 모듈명을 호출명으로 가져올 수 있다.
