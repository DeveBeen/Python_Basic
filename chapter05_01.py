# Chapter05-1
# 파이썬 함수 및 중요성
# 함수의 중요성 : 프로그램의 흐름을 함수 단위로 나워서 보기 쉽고, 함수별로 나누어진 프로그램은 하나의 함수에 집중하기 때문에 안전성이 좋다. 또, 사용한 기능을 중복으로 사용할 때 좋다.
# 파이썬 함수식 및 람다(Lambda)

# 함수의 정의 방법
# def function_name(parameter):
#   code

# 예제 1
def first_func(w1): # 괄호 안에 원하는 인수를 선언하여 인수를 활용하여 함수를 선언한다. (물론 빈칸으로 두어 선언도 가능하다.) -> 함수선언
    print('Hello, ', w1)

word = 'Goodboy'

first_func(word) # 함수를 호출하는 방식이다. 여기선 괄호안에 word를 호출하였으니, w1인수에 word인수가 들어가 위에서 선언한 함수가 실행되었다. -> 함수호출

# 예제 2
def return_function(w1):
    value = "Hello, " + str(w1)
    return value # value 인수를 함수 내에서 따로 선언하여 return으로 값 자체가 빠져나가는 함수이다.

x = return_function('Goodboy2') # 이처럼 함수 호출을 이용하여 변수를 선언하였으므로, return_function에 의해 x에 'Hello, Goodboy2'라는 값이 들어간다.
print(x) # 위에서 말한 값이 들어가 출력됨을 알 수 있다.

# 예제 3 (다중반환)
def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3 # 이처럼 다중반환으로 여러 값을 동시에 반환 시킬 수 있다.

x, y, z = func_mul(10) # 함수는 일대일 대응이여야 하므로, 다중으로 값이 나오면 받는 인수도 그와 같은 개수여야 한다. (언팩킹)

print(x, y, z)

# 예제 4 (튜플 리턴)
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3) # 이처럼 return값의 자료형을 정해서 반환도 가능하다.

q = func_mul2(20)

print(type(q), q, list(q)) # 튜플로 '팩킹'이 되었음을 알 수 있다. 또, list() 등 따른 자료형으로 변환시켜서 추출도 가능하다.

# 예제 5 (리스트 리턴)
def func_mul3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]

p = func_mul3(30)

print(type(p), p, set(p)) # 위와 같은 방식으로 실행된다.

# 예제 6 (딕셔너리 리턴)
def func_mul4(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'v1' : y1, 'v2' : y2, 'v3' : y3}

d = func_mul4(30)

print(type(d), d, d.get('v2'), d.items(), d.keys())

# 중요
# *args, **kwargs

# *args(Unpacking)
def args_func(*args): # '*' 몇개의 인자가 호출되든 튜플형으로 받아주는 매개변수이다.
    for i, v in enumerate(args): # enumerate() : 튜플형 인자를 각각의 원소로 언팩킹하여 반환하는 함수 (인덱스 순서로 언팩킹된다.)
        print('Result : {}'.format(i), v) # format을 사용하여, i:index번호, v:value실제값을 출력해준다.
    print('-------') # 튜플형태가 넘어왔을 떄, 많이 사용함.

args_func('Lee') # 함수 args_func(args)처럼 별 기호('*')가 없었으면 하나의 문자열(시퀀스)로 인식, 각각의 문자 'L','e','e'가 출력된다. 하지만 여기선 '*'로 인해서 0 : Lee가 통체로 출력된다.
args_func('Lee', 'Park') # 하지만 '*'로 붙어 매개변수 표시를 하였기 때문에, 다중 변수가 하나의 매개변수 안에 들어가도 언팩킹되어, 'Lee'와 'Park'를 따로따로 출력해준다, 만약 '*' 없다면, 함수를 선언할 때 (a, b, c ... )처럼 다중으로 받아, 일대일 대응 함수로 만들어야 한다.
args_func('Lee', 'Park', 'Kim') # 이처럼 몇 개가 쌓여 있든 이를 튜플형으로 인식하여 언팩킹 해준다.

# **kwargs(Unpacking)
def kwargs_func(**kwargs): # '**' 호출된 인자를 딕셔너리형으로 받아주는 매개변수이다.
    for v in kwargs.keys():
        print('{}'.format(v), kwargs[v]) # 위처럼 이또한 언팩킹 함수이다. 이는 딕셔너리 형으로 format을 통하여 key를 받고, 뒤에는 값을 받았다.
    print('-------') # 딕셔너리는 순서가 존재하지 않아 key가 인덱스 번호와 비슷하므로 위 함수와 다른게 없다.

kwargs_func(name1 = 'Lee')
kwargs_func(name1 = 'Lee', name2 = 'Park')
kwargs_func(name1 = 'Lee', name2 = 'Park', name3 = 'Cho') # 딕셔너리형도 원소의 개수 상관없이 언팩킹을 해준다.

# 전체 통합
def example(args_1, args_2, *args, **kwargs): # 이처럼 여러개 인자를 동시 선언 후 사용도 가능하다.
    print(args_1, args_2, args, kwargs)

example(10, 20, 'Lee', 'Kim', 'Park', age1 = 20, age2 = 30, age3 = 40) # 10과 20은 일대일대응으로 example함수 args_1과 args_2에 할당, 그 이후 문자열은 args의 튜플형으로 할당 후 key = value 형태인 인자는 kwargs에 딕셔너리로 할당된다.

# 중첩함수 : 함수 안에 함수가 있는 형태 <-> 함수형 프로그램
def nested_func(num):
    def func_in_func(num): # 여기에 num + 100이 들어가고
        print(num) # num + 100이 출력된다.
    print('In func') # func_in_func 함수는 선언만 되었고 호출되지 않았으므로 'In func'가 먼저 출력된다.
    func_in_func(num + 100) # 여기서 func_in_func가 선언되었으므로 입력된 num = num + 100이 되어 위로 올라가 (101줄로)

nested_func(100) # 위 함수 시스템에 따라 최종적으로 num + 100이 출력되므로 200이 출력된다.
#func_in_func(100) -> 이처럼 만약 밖에서 호출 한다고 한다면, 함수 선언이 안된 상태이기 때문에 호출이 되지 않는다.

# 람다식 예제
# 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화
# 남발 시 가독성 오히려 감소
#def mul_func(x, y):
#    return x * y
#lambda x, y: x * y  이것이 lambda함수이다. 위에 mul_func와 같은 함수이나, 이 함수는 함수의 이름이 없다. 이는 변수의 담아서 사용하거나 함수의 인자로 사용하기도 한다.
def mul_func(x, y):
    return x * y

# 일반적 함수 -> 변수의 할당
print(mul_func(10, 50)) # 위 함수의 호출 방식은 이러하다.
mul_func_var = mul_func # 이는 변수의 함수를 할당하는 방식으로
print(mul_func_var(20, 50)) # 할당 후에 이와같이 사용할 수 있다.

# 람다 함수 -> 변수에 할당
lambda_mul_func = lambda x,y : x*y # lambda함수는 즉시 실행 함수이므로 이처럼 선언과 호출이 동시에 가능하다.
print(lambda_mul_func(50, 50)) # 이처럼 출력한다. 단순한 코드의 유리하다.

def func_final(x, y, func):
    print(x * y * func(100, 100))

func_final(10, 20, lambda x,y:x*y) # 함수를 인자로 받는 함수에 lambda함수를 할당하여 즉시 실행이 가능하다. 보통 람다는 이럴 때, 많이 사용한다.
func_final(10, 20, mul_func_var) # 물론 이처럼 일반 함수를 할당한 변수를 할당해도 함수가 정상적으로 실행된다.
