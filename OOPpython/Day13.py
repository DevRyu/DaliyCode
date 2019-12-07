# 4-5
# 파이썬 함수의 특징
# 클로저와 데코레이터

# 파이썬 변수 범위 (global)

# 지역변수와 전역변수가 같은 이름으로 선언이 되어있는데 출력 후에 변수를 넣어주면 어떨까?


# Case 1 전역 변수를 함수에서 호출 시 결과

# b = 1
# def func1(a):
#     print(a)
#     print(b)

# from dis import dis

# print(dis(func1))
#  10           0 LOAD_GLOBAL              0 (print)
#               2 LOAD_FAST                0 (a)
#               4 CALL_FUNCTION            1
#               6 POP_TOP

#  12           8 LOAD_GLOBAL              0 (print)
#              10 LOAD_GLOBAL              1 (b)  # b를 호출한다.
#              12 CALL_FUNCTION            1
#              14 POP_TOP
#              16 LOAD_CONST               0 (None)
#              18 RETURN_VALUE
# None
# 3
# 1


# Case 2) 지역 변수 호출시 지역변수 b 선언, 할당 이전시의 결과(에러)

b = 1
def func1(a):
    print(a)
    print(b)
    b = 2 # UnboundLocalError: local variable 'b' referenced before assignment  로컬 변수는 할당 전에 참조된다. 
    # 이름이 같은 지역변수와 전역변수가 공존시 함수 내 작동에서 지역 변수가 변수로써 사용이된다. 

from dis import dis

print(dis(func1))

#  40           0 LOAD_GLOBAL              0 (print)
#               2 LOAD_FAST                0 (a)
#               4 CALL_FUNCTION            1
#               6 POP_TOP

#  41           8 LOAD_GLOBAL              0 (print)
#              10 LOAD_FAST                1 (b)
#              12 CALL_FUNCTION            1
#              14 POP_TOP

#  42          16 LOAD_CONST               1 (2)
#              18 STORE_FAST               1 (b)
#              20 LOAD_CONST               0 (None)
#              22 RETURN_VALUE
# None
# 2



# 클로저 
# 반환되는 내부 함수에 대해서 선언된 연결을 가지고 참조
# 반환 당시의 함수의 유효범위를 벗어난 변수 또는 메소드에 직접 접근 가능 


# 클로저를 쓰지않고 기존의 클래스 사용시

class Average():
    def __init__(self):
        self._series = []

    def __call__(self, v):
        self._series.append(v)
        print('{} {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)

# 인스턴스 생성
cls_test =Average()
print(cls_test(1))
print(cls_test(5))
print(cls_test(9))
# 호출 할 때마다 값을 더하고 나눠준다.
# [1] 1
# 1.0
# [1, 5] 2
# 3.0
# [1, 5, 9] 3
# 5.0


# 클로저(Closure) 사용시
# 장점 : 전역변수 사용감소, 디자인 패턴 적용, 변수 은닉화 가능 
# 단점 : 자유 변수영역이 함수 실행, 또는 사용시 메모리에 적재되므로 메모리에 과다하게 사용되어 질 수 있다. 
def easy_closure():
    # ------------외부함수와 내부함수의 영역 = 자유 변수영역 시작 ------------
    series = []
    # ------------- 자유영역 종료-----------------------------
    def easy_average(v):
        series.append(v)
        print('{} {}'.format(series, len(series)))

        return sum(series) / len(series)    
    # easy_closure 함수가 밑에서 실행 되었다고 가정하고 easy_average를 반환 해서 클로저가 선언 되었지만
    # 여전히 자유 변수 영역을 사용할수 있다.
    return easy_average

# 클로저 선언
closure1 = easy_closure()

print(closure1(5))
print(closure1(10))
print(closure1(15))

#__code__ : 특수 속성으로 함수의 body를 나타내는 코드 객체
# dir()로 열면 co_freevars(자유 변수 영역) 이 나온다.
print(dir(closure1.__code__))

# co_freevars를 출력하면 튜플 형태로 자유 변수 영역에 저장되어있다.
print(closure1.__code__.co_freevars) # ('series',)

# 클로저에도 함수처럼 내장 메서드, 속성이 정의 되어있고 
print(dir(closure1.__closure__))

print(closure1)
# 클로저에도 함수처럼 내장 메서드, 속성이 정의 되어있고
print(dir(closure1.__closure__[0].cell_contents)) # 인덱스[0]으로 주면 셀로 리턴이되는데 셀이란 스프레드 시트의 셀타입이다. "셀" 객체는 여러 스코프에서 참조하는 변수를 구현하는 데 사용됩니다.
# 조금 더 쉽게 찾아본 결과 Cpython에서 렉서(어휘 분석) 환경에서 클로저의 어휘(cell)이라고 생각하시면 될거 같습니다.
# cell_contents속성을 사용하면 클로저의 사용가능한 함수들을 보여준다. 
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'] 
# Contains the data for one cell. (XFCell is the base class of Cell)
# WARNING: You don’t call this class yourself. You access Cell objects via methods of the Sheet object(s) that you found in the Book object that was returned when you called open_workbook().


# 잘못된 클로저의 사용 예

def Average2():
 
    # free 영역
    cnt   = 0 
    total = 0

    def easy_average2(v):
        
        # 클로저 영역
        cnt += 10
        total += v
        return total / cnt
    return easy_average2

closure2 = Average2() 

# free영역에서 정의되어있으면 클로저 영역에서 위의 free 영역을 참조해서 할까?

# 위의 질문의 답은 틀렸다. scope의 문제가 생긴다. free영역의 참조를 명시해줘야한다.
# print(closure2(2)) # UnboundLocalError: local variable 'cnt' referenced before assignment


def Average2():
 
    # free 영역
    cnt   = 0 
    total = 0

    def easy_average2(v):
        
        nonlocal cnt, total
        # 클로저 영역
        cnt += 10
        total += v
        return total / cnt
    return easy_average2

closure2 = Average2() 

print(closure2(2)) # 2 / 10 == 0.2 가 잘 출력이 된다.




# 데코레이터는 클로저의 확장판이라고 생각해도 된다.
# 장점 : 중복 제거, 코드간결, 클로저 보다 문법 간결, 조합해서 사용 용이
# 단점 : 디버깅 어려움, 에러의 모호함

# 내가 짠 함수의 성능을 시간으로 보고 싶으면?

import time

def clock(func):

    def clocked(*args):
        # perf_counter()는 time에 있는 퍼포먼스 카운터의벤치마크이다.
        start_time = time.perf_counter()
        result     = func(*args)
        end_time   = time.perf_counter() - start_time

        # 함수명
        name = func.__name__

        # 튜플 컴프리핸션으로 매개 변수 출력
        arg_str = ','.join(repr(arg) for arg in args)
        
        # 걸린 사간, 함수 명, 매개변수들, 결과 값 출력
        print('result : [%0.5fs] %s(%s) -> %r' % (end_time, name, arg_str, result))

        return result
    return clocked

# 일반적인 함수들 위에, 위에서 정의한 데코레이터 들을 실행해서 시간(퍼포먼스)을 체크할 수 있다. 

# 간단한 함수를 3개를 테스트 해

# 잠깐동안 프로세스를 멈추는 함수
def time_func(seconds):
    time.sleep(seconds)

# 더한 결과값을 출력하는 함수
def sum_func(*numbers):
    return sum(numbers)

# 팩토리얼을 구하는 함수 
def fact_fun(n):
    return 1 if n < 2 else n * fact_fun(n-1)




# 데코레이터 미사용 시

not_deco1 = clock(time_func)
print(not_deco1) #     def clocked(*args): 가 들어있다.
print(not_deco1.__code__.co_freevars) # ('func',) 가 코드 자유영역 안에 있다.
print(not_deco1(2)) # result : [0.00001s] sum_func(200) -> 200

not_deco2 = clock(sum_func) 
print(not_deco2) #     def clocked(*args): 가 들어있다.
print(not_deco2.__code__.co_freevars) # ('func',) 가 코드 자유영역 안에 있다.
print(not_deco2(200)) #위와 동일
print(not_deco2(200, 200, 200, 200, 200)) # result : [0.00000s] sum_func(200,200,200,200,200) -> 1000

not_deco3 = clock(fact_fun)
print(not_deco3) #     def clocked(*args): 가 들어있다.
print(not_deco3.__code__.co_freevars) # ('func',) 가 코드 자유영역 안에 있다. 

print(not_deco3(500))# result : [0.00126s] fact_fun(500) -> 12201368259911100687012387
# 팁 - 파이썬은 코더의 실수로 순회가 무한 반복을 막기위해 내부에 반복(Recursion)이 가능한 횟수를
# 기본 2000이하로 잡아 놓았다 
# 위를 해결 할려면 sys영역에서  Recursionlimit을 설정해줌으로서 해결이 가능하다

# import sys
# sys.setrecursionlimit(10000) 




# 데코레이터 사용시
# @함수 형태로 사용하면 됩니다.

@clock
def time_func(seconds):
    time.sleep(seconds)

# 더한 결과값을 출력하는 함수
@clock
def sum_func(*numbers):
    return sum(numbers)

# 팩토리얼을 구하는 함수 
@clock
def fact_fun(n):
    return 1 if n < 2 else n * fact_fun(n-1)

#실행은 원형의 함수로 실행

print(time_func(2)) # result : [2.00209s] time_func(2) -> None

print(sum_func(200, 200, 200, 200, 200)) # result : [0.00000s] sum_func(200,200,200,200,200) -> 1000

print(fact_fun(100))# result : [0.00000s] fact_fun(1) -> 1
# result : [0.00002s] fact_fun(2) -> 2
# result : [0.00003s] fact_fun(3) -> 6
# result : [0.00004s] fact_fun(4) -> 24
# result : [0.00005s] fact_fun(5) -> 120
# result : [0.00006s] fact_fun(6) -> 720
# result : [0.00007s] fact_fun(7) -> 5040
# result : [0.00129s] fact_fun(100) -> 9332621544394415268169923885626
