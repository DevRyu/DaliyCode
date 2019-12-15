# 파이썬 함수의 특징
# 일급 함수(일급 객체)


# 모든 자료형은 객체이다. 

# 그래서 파이썬은 순수 객체지향 언어이다.

# 함수는 그 중에서도 일급 시민(first-class citizen)이다. 

# 일급 시민(first-class citizen)의 의미는 :

# 런타임 초기화, 변수등에 할당 가능(데코레이터, 클로저), 함수 인수 전달 가능(ex) 제약조건 len=10 등), 함수 결과로 반환 가능


# 클래스와 함수간의 차이는 무엇인가? 라고 물으면 쉽게 답 할수 있을까?
# 구조적 차이는 쉽게 설명이 가능 하다.
# 함수는 행위만을 가지며 클래스는 속성과 행위를 가진다.  
# 그렇다면 세부적으로 파이썬에서는 이 둘 사이에 기능적인 차이는 무엇인가?
# 그 질문은 던지기 전에 파이썬의 자료들은 모두 객체라고 저번에 명시했엇다.

# 함수는 객체인가?
#  예제
def Fac():
    return None

class F:
    def fac():
        return None

# 함수든 클래스든 모두 객체이다.
print(type(Fac), type(F)) #<class 'function'> <class 'type'>

# 그렇다면 파이썬에서 함수와 클래스가 가지는 내부적 기능의 차이는 어떤 것 일까?

# 클래스에 없는 함수만의 고유한 특징은 아래이다.
# {'__annotations__', '__defaults__', '__qualname__', '__call__', '__kwdefaults__', '__name__', '__globals__', '__get__', '__code__', '__closure__'}
print(set(sorted(dir(Fac))) - set(sorted(dir(F)))) 

print()

# 함수에는 없는 클래스 만의 특징은 아래이다.
print(set(sorted(dir(F))) - set(sorted(dir(Fac))))
# {'__weakref__'}

# 1. 변수에게 함수 할당하기

def factorial(n):
    '''
    factorial function
    n : int
    '''
    if n == 1:
        return 1
    return n * factorial(n-1)

f1_func = factorial(5) # return이 int여서 함수가 아닌 정수(int)반환
f2_func = factorial # 함수가 변수에 할당됨

print(type(f1_func), type(f2_func)) # <class 'int'> <class 'function'>
print(f1_func, f2_func) # 120 <function factorial at 0x7fa70784c7a0>

# 위의 f2_func는 인자를 가지는 함수다 

# 하지만 인자가 없는 함수는 어떨가?

def fake_factorial():
    a = 1
    b = 2
    return a
f3_func = fake_factorial() 
f4_func = fake_factorial

# 예상 했던 결과값을 가진다. 단지위 f1_func는 파라미터 없이 factorial()을 할당하지 못한다. 
print(type(f3_func), type(f4_func)) # <class 'int'> <class 'function'>


# 다시 factorial함수를 할당하자

f5_func = factorial
# 할당된 변수를 map함수를 사용해서 for문과 같이 돌릴 수 있다.

print(list(map(f5_func, range(1,6)))) # [1, 2, 6, 24, 120]



# 함수 인수를 전달하고 함수로 결과를 반환하는 함수를 고위 함수라고 한다 (Higer Order Function)

# 함수안의 함수를 사용해보자
# 홀수 차례인 1,3,5 인자인 것만 return하는 함수
print(list(map(f5_func, filter(lambda x : x % 2, range(1,6))))) # [1, 6, 120]
print([f5_func(i) for i in range(1, 6) if i % 2]) # [1, 6, 120]

from dis import dis

# 위의 함수를 비교해보자
print(dis('list(map(f5_func, filter(lambda x : x % 2, range(1,6))))'))

#   1           0 LOAD_NAME                0 (list)
#               2 LOAD_NAME                1 (map)
#               4 LOAD_NAME                2 (f5_func)
#               6 LOAD_NAME                3 (filter)
#               8 LOAD_CONST               0 (<code object <lambda> at 0x7fdbeb078030, file "<dis>", line 1>)
#              10 LOAD_CONST               1 ('<lambda>')
#              12 MAKE_FUNCTION            0
#              14 LOAD_NAME                4 (range)
#              16 LOAD_CONST               2 (1)
#              18 LOAD_CONST               3 (6)
#              20 CALL_FUNCTION            2
#              22 CALL_FUNCTION            2
#              24 CALL_FUNCTION            2
#              26 CALL_FUNCTION            1
#              28 RETURN_VALUE

# Disassembly of <code object <lambda> at 0x7fdbeb078030, file "<dis>", line 1>:
#   1           0 LOAD_FAST                0 (x)
#               2 LOAD_CONST               1 (2)
#               4 BINARY_MODULO
#               6 RETURN_VALUE
# None


print(dis('[f5_func(i) for i in range(1, 6) if i % 2]'))

#   1           0 LOAD_CONST               0 (<code object <listcomp> at 0x7f21f01a0810, file "<dis>", line 1>)
#               2 LOAD_CONST               1 ('<listcomp>')
#               4 MAKE_FUNCTION            0
#               6 LOAD_NAME                0 (range)
#               8 LOAD_CONST               2 (1)
#              10 LOAD_CONST               3 (6)
#              12 CALL_FUNCTION            2
#              14 GET_ITER
#              16 CALL_FUNCTION            1
#              18 RETURN_VALUE

# Disassembly of <code object <listcomp> at 0x7f21f01a0810, file "<dis>", line 1>:
#   1           0 BUILD_LIST               0
#               2 LOAD_FAST                0 (.0)
#         >>    4 FOR_ITER                20 (to 26)
#               6 STORE_FAST               1 (i)
#               8 LOAD_FAST                1 (i)
#              10 LOAD_CONST               0 (2)
#              12 BINARY_MODULO
#              14 POP_JUMP_IF_FALSE        4
#              16 LOAD_GLOBAL              0 (f5_func)
#              18 LOAD_FAST                1 (i)
#              20 CALL_FUNCTION            1
#              22 LIST_APPEND              2
#              24 JUMP_ABSOLUTE            4
#         >>   26 RETURN_VALUE
# None

# 리스트 컴프리핸션이 훨신 더 빠르다.

# reduce() 함수 개념

from functools import reduce
from operator  import add # 오퍼레이터의 더하기 기능을 가져온다.


# reduce함수는 원소들을 중첩(누적)하여 하나로 만드는 과정 왼쪽으로부터 오른쪽까지의 single values를 합치는것입니다.
# 함수, iter한 자료형을 파라미터로 받습니다.

print(reduce(add, range(1,11))) # (((1+2)+3)+4)......10  = 55

# 익명함수 (람다)
# 다른 개발자가 알수 있도록 주석을 작성해준다
# 가독성을 위해 일반 함수 형태로 리펙토링 권장

print(reduce(lambda i,j : i + j , range(1,11))) #  55
# callable() : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인가능하다.

print(callable(str), callable(list), callable(add)) # True ,True, True
# 위에서 쓴 add도 callable 함으로 인자로 사용이 되었다.

# class as callable()

# 그렇다면 위의 add를 lambda로 구현 햇는데 
# 클래스를 callable하게 구현하여 lambda를 대처하는 클래스를 만들어 볼 수 있을까?

# 첫번째는 그냥 클래스의 메서드에 직접 접근하여 구해버리는 방법
class Add:

    # 덧샘을 리턴하는 함수
    def add(self,i,j):
        return i+j

add__ = Add()
print(reduce(add__.add,  range(1,11))) # 55

# 두번째는 callable(__call__)을 활용하여 사용하기
class Add2:

    # 덧샘을 리턴하는 함수
    def add(self,i,j):
        return i+j

    # callable
    def __call__(self,i,j):
        return self.add(i,j)

add__ = Add2()
print(reduce(add__,  range(1,11))) # 55



# 다양한 매개변수 입력시 파이선의 처리방법

def test(id, *args, age=None, **kwargs):
    return 'test ({}) ({}) ({}) ({})'.format(id, args, age, kwargs)


print(test('test1'))
# test (test1) (()) (None) ({})
# 아이디 매개변수로만 받는다.

print(test('test1', 'test2'))
# test (test1) (('test2',)) (None) ({})
# 아이디 매개변수 먼저 붙이고 나머지는 튜플로 가변인자로 

print(test('test1', 'test2', 'test3'))
# test (test1) (('test2', 'test3')) (None) ({})
# 아이디 매개변수 먼저 붙이고 나머지는 튜플로 가변인자로 

print(test('test1', 'test2', 'test3'))
# test (test1) ((['test2', 'test3'],)) (None) ({})
# 아이디 매개변수 먼저 붙이고 나머지는 튜플내 리스트 가변인자로 

print(test('test1', 'test2', 'test3', age=7))
# test (test1) (('test2', 'test3')) (7) ({})
# 아이디 매개변수 먼저 붙이고 나머지는 튜플로 가변인자로 age 디폴트값 변함

print(test('test1', 'test2', 'test3', age=7, name='abc'))
# test (test1) (('test2', 'test3')) (7) ({'name': 'abc'})
# 아이디 매개변수 먼저 붙이고 나머지는 튜플로 가변인자로 age 디폴트값 변함 name은 없는 파라미터로 키워드 인자 처리

# print(test('test1', 'test2', 'test3', age=7, name='abc', 'test4'))
# 'test4' 같은 경우 가변인자로 처리되어야 하는데 키워드 인자 뒤에있으므로 순서를 지켜줘야 한다. SyntaxError: positional argument follows keyword argument

print(test('test1', 'test2', 'test3', age=7, password='1234', name='abc'))
# test (test1) (('test2', 'test3')) (7) ({'password': '1234', 'name': 'abc'})

# 값만 인자로 넣을경우 가변인자 처리
# 값이 아닌 키 벨류 형식으로 줄시 키워드 인자처리 

# 함수 Signatures
# 함수 내의 파라미터의 정보를 볼 수 있다.

from inspect import signature

sg = signature(test)

print(sg)
# (id, *args, age=None, **kwargs)
print(sg.parameters)
# 더 자세히 파라미터의 정보를 볼수있다.
# OrderedDict([('id', <Parameter "id">), ('args', <Parameter "*args">), ('age', <Parameter "age=None">), ('kwargs', <Parameter "**kwargs">)])

# 모든 정보 출력하려면 for문으로 items()의 name 과 param의 kind와 default가 있는지 없는지 확인 가능하다.
for name, param in sg.parameters.items():
    print("name: ", name, "kind: ", param.kind,"default :", param.default)
# name:  id kind:  POSITIONAL_OR_KEYWORD default : <class 'inspect._empty'>
# name:  args kind:  VAR_POSITIONAL default : <class 'inspect._empty'>
# name:  age kind:  KEYWORD_ONLY default : None
# name:  kwargs kind:  VAR_KEYWORD default : <class 'inspect._empty'>
# sql의 컬럼 정보와 많이 닮아 있다.


# partial 사용법 : 인자를 고정하기위해서 
# 주로 특정 인수 고정 후 콜백 함수에서 사용한다.
# 콜백 함수는 일급함수(first-class function)내에 포함된 
# 일급 시민의 기능중  "함수 인수 전달 가능"과 같다.
# 파이썬과 비슷한 JS MDN자료를 참조해서 파이썬의 구조와 비교해 본 결과 내린 결론이여서 틀릴 수도 있다.
# (그래도 구조적으로 보았을때 맞는거 같다.)
# 파이썬 콜백 예시를 들면 이런 거다. 

# https://developer.mozilla.org/ko/docs/Glossary/First-class_Function

from operator import mul
from functools import partial

print(mul(5,5))
# 굳이 5*5를 쓰지 않는 것은
# prtial()함수로 mul 함수를 첫 번째 인자로 받기 위해서

# prtial 인자 고정하는 함수
five = partial(mul, 5)
# 5 * ?와 같이 첫번째 인자를 고정할수있다.

# 두번째 변수 고정 추가를 파티션 함수로 받아서 또 쓸수 이싿.
five_second = partial(five, 5)

print(five(5)) # 인자 2개중 첫번째만 5로 고정되있고 뒤에 인자를 5를 넣음 # 25
print(five_second()) # 25

# 아래처럼 리스트 컴프리핸션도 가능하다.
print([five(i) for i in range(1,11)]) # [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
print(list(map(five, range(1,11))))   # [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]