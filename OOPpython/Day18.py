# 코루틴 개념

# 파이썬에서 쓰래드, 태스크, 프로세스를 사용해서 동시적으로 작업들을 처리한다.
# https://ingorae.tistory.com/473
# 쓰레드(thread)    : 스레드는 프로그램 내에서 실행되는 흐름의 단위
# 태스크(task)      : 파이썬에서의 테스크 : 태스크(asyncio.Task)는 asyncio.Future의 파생 클래스이며 asyncio.Future의 기능과 실행할 코루틴의 객체를 포함, 태스크는 코루틴의 실행을 취소하거나 상태 확인, 완료 및 결과 설정에 사용
#                   : 운영체제에서의 테스크 :  일괄처리 시절 당시의 작업 단위, 작개는 테스크를 프로세스라고 부름 
# 프로세스(process) : CPU에 의해 처리되는 사용자 프로그램, 시스템 프로그램 즉 실행중인 작업단위, 상위에 코어 개념이 있음
# 동시성 : 순차적으로 일을 처리 하는 것이 아닌 동시에 여러가지일을 할수 있는것, 분기를 처리해서 효율을 극대화
# 병렬성 : 하나의 계산을 여러개의 쓰레드들이 처리하 하는것(병렬처리라고도 함)

# https://nachwon.github.io/asyncio-futures/
# 파이썬에서의 동시성과 병렬성 : 1.쓰래드를 사용하는 threading 모듈         (하나의 프로세서) (동시성) 
#                              2.태스크를 사용하는 asyncio 모듈           (하나의 프로세서) (동시성)
#                              3.프로세스를 사용하는 multiprocessing 모듈 (다중의 프로세서) (병렬성)

# 1-1. threading 모듈은 운영체제가 언제든 멈추고 돌아간다. 
#      다시 말해 운영체제가 쓰레드 선점이 가능해서 선점형 멀티태스킹(pre-emptive multitasking)이라고 부른다.
#      멀티태스킹 실행중 프로그래머가 아무것도 안해도 쓰레드 스위칭이 일어나지만 역으로 스위칭이 일어나서 다루기 어려워 질 수 도 있다.
# 2-1. asyncio 모듈은 각 테스크가 언제 스위칭을 할지 명시를 함으로 코드를 수정한다. 
#      협력식 멀티태스킹(cooperative multitasking)이라고 부른다.
#      유저가 코드를 어떻게 처리할지 코드 수정이 필요한 부분이 생길 수 있다. 
# 3-1. 하나가 아닌 여러 프로세스로 작업을 하는 것을 multiprocessing 모듈이라고 한다. 
# GIL(글로벌 인터프리터 락) 이라는 이유로 파이썬에서는 멀티 쓰레딩을 지원 못하고 멀티 프로세싱과, 비동기 처리로 병렬성과 동시성을 해결함으로 성능 향상을 하려고 한다.
# 내용이 너무 길어짐으로 나중에 포스팅 하겠다.
# https://dgkim5360.tistory.com/entry/understanding-the-global-interpreter-lock-of-cpython
# https://velog.io/@doondoony/Python-GIL
# https://118k.tistory.com/606


# 제너레이터 vs 코루틴
# yield 키워드 : 메인루틴 <-> 서브루틴 사이를  제어합니다
# 코루틴 제어, 코루틴 상태 , 양방향 값 전송
# 메인루틴 : 파이썬 스크립트를 위에서 아래로 순차로 실행합니다. 하나의 흐름이라고 이해하세요
# 서브루틴 : 메인루틴에서  함수가 실행이 되면 다시 위의 함수로직을 읽고 리턴하는 과정이라고 생각하세요
# 코루틴   : 루틴 실행 중 멈추는게 가능합니다. 
#         : 특정 위치로 갔다가 원래 위치로 돌아 가서 코드를 실행하는게 가능합니다.
#         : 동시프로그래밍(동시성)이 가능합니다.
#         : 코루틴은 한개의 쓰레드에서 진행될떼 스케쥴링 오버헤드가 매우 적습니다.
# 쓰레드   : 위의 개념은 싱글 쓰레드에서도 돌아가지만 멀티 쓰레드 사용시 자원이 공유가됩니다.
#            :교착상태(deadlock),컨텍스트 스위칭 시간 비용추가,자원 소비 증가 같은 단점도 고려해야합니다.


# 이전에는 yield를 반환만 했습니다. 
# 예를 들어 yield 'aaa' 처럼 말이죠
# 하지만 yield값을 받을수도 있습니다(넣는다)

# 라이브러리를 사용하기 전에 코루틴을 직접 만들어서 배워봅시다.
def corou1() :
    print('start')
    i = yield # 메인루틴에서 yield값을 받는다. 
    print('recived : {}'.format(i))

# 위의 함수를 제너레이터로 선언 해보겠습니다.
# 저번글을 보신분은 알겠지만 함수안에 yield키워드가 있으면 제너레이터로 반환 됩니다 

c1 = corou1()
print(type(c1)) # <class 'generator'>

# yield 실행 전까지 진행
next(c1) # start //

# 실행된 부분
# def corou1() :
#     print('start')
#     i = yield

# next(c1) # 밑의 예제를 할려면 주석 처리를 해야합니다.

# 실행된부분
#    print('recived : {}'.format(i))
# recived : None

# StopIteration 에러가 호출됩니다.
# Traceback (most recent call last):
#   File "Day18.py", line 59, in <module>
#     next(c1)
# StopIteration

# 어떤 기본 값의 파라미터나 인자가 없으니 기본으로 None을 전달합니다.
def corou2() :
    print('start')
    i = yield # 메인루틴에서 yield값을 받는다. 
    print('recived : {}'.format(i))

c2 = corou2()
# 이 제너레이터에 값을 보내주는 아주 신박한 함수가 있습니다.
next(c2)
# c2.send(100)  # 밑의 예제를 할려면 주석 처리를 해야합니다

# 실행 된 부분 
# 값을 받았군요!
# recived : 100
# Traceback (most recent call last):
#   File "Day18.py", line 81, in <module>
#     c1.send(100)
# StopIteration

def corou3() :
    print('start')
    i = yield # 메인루틴에서 yield값을 받는다. 
    print('recived : {}'.format(i))

c3 = corou3()
# next(c3)를 실행하지 않고 c3.send(100)을하면 yield가 준비되지 않았으므로 에러가 출력이 됩니다.
# 어셉블리 관점으로 본다면 자료형이 선행 load가 안 되었는데 값을 넣어 줄려 한거와 비슷한 상황입니다.  
# c3.send(100) # TypeError: can't send non-None value to a just-started generator

# 파이썬s에서 제공하는 코루틴의 상태를 확인하는 상태코드에 대해 알아 보겠습니다.
# GEN_CREATED   : 처음 대기 상태입니다.
# GEN_RUNNING   : 실행 상태입니다.
# GEN_SUSPENDED : yield 대기 상태입니다.
# GEN_CLOSED    : 실행 완료 상태입니다.

# 상태코드 사용법을 예제를 통해 알아보겠습니다.

def corou4(x) :
    print('start {}'.format(x))
    i = yield x # x 파라미터를 받습니다.
    print('recived : {}'.format(i))
    j =  yield x + i
    print('recived : {}'.format(j))

c4 = corou4(100)

from inspect import getgeneratorstate
# 아직 제너레이터 내 실행이 안된 만들어지지 않는 초기 대기상태
print(getgeneratorstate(c4)) # GEN_CREATED 

print(next(c4))# start 100 100
# # 함수내 실행 된 코드
#     print('start {}'.format(x))  # start 100
#     i = yield x # x 파라미터를 받습니다. # 100


# yield 대기 상태
# 'yield x'까지는 실행되엇고
# 'i = '값을 받기위해 대기 상태라고 생각하시면 됩니다.
print(getgeneratorstate(c4)) # GEN_SUSPENDED

# 'i = 40'값을 보내봅시다.
print(c4.send(30)) # recived : 30 # 130
    # print('recived : {}'.format(i))
    # j =  yield x + i
    # 'yield x + i'까지는 실행되엇고
    # 'j = '값을 받기위해 대기 상태라고 생각하시면 됩니다.

print(getgeneratorstate(c4)) # GEN_SUSPENDED

# print(c4.send(70)) #recived : 70
# 더 이상 실행 될 코드가 없으므로 
# 실행이StopIteration 끝나는 에러가 발생한다.
# 나중에 asyncio에서는 에러가 처리안되고 끝납니다.

print('-------------')

# 코루틴 데코레이터 패턴 예시를 만들어 보겠습니다.
# wrap을 쓰겟습니다.
from functools import wraps

# 코루틴을 하나 만들어 봅시다 
def coroutine(func):
    '''Decorator'''
    @wraps(func) # 외부의(def coroutine(func)와 def primer사이의) 것들을 감싸는 데코레이터, 없어도 동작합니다.
    def primer(*args, **kwargs): # 딕셔너리, 튜플, 리스트등 아무거나 사용가능
        gen = func(*args, **kwargs)  # 함수 실행
        next(gen) # next()를 한번 호출하겠습니다. 
        # next() 하는 이유는 위에서 보았 듯 next() 이 후로 yield가 준비되기 떄문에 
        # 후에 스크립트에서 send()를 바로 사용이 가능하게 하기 위함 입니다.
        return gen 
    return primer #클로저입니다.
# 더하는 일반 제너레이터 함수 입니다.

@coroutine
def sumfunc():
    total = 0
    term  = 0
    while True:
        term = yield total
        total += term

 # 제너레이터 생성후
s1 = sumfunc() 

# 하나 하나씩 넣어 보겠습니다.
print(s1.send(100)) # 100
print(getgeneratorstate(s1)) # GEN_SUSPENDED
print(s1.send(40)) # 140
print(getgeneratorstate(s1)) # GEN_SUSPENDED
print(s1.send(60)) # 200
print(getgeneratorstate(s1)) # GEN_SUSPENDED


# 코루틴 예외처리 함수를 실행 해 보겠습니다.

# 예외 클래스
class Except_(Exception):
    '''예외 유형'''

# 예외 함수
def coroutine_except():
    print('started')
    try:
        
        while True:
            try:
                print('?')
                x = yield
                print('??')

            # 위의 선언한 예외 클래스 호출 
            except Except_:
                print('Except_ Class that i defined, occurred')
            
            # 예외가 발생하지 않았다면 실행 
            else :
                print('received : {}'.format(x))
    # 위의 try가 문제 없이 끝나면 출력한다.
    finally:
        print('-> ending')

exe_co = coroutine_except() # 제너레이터를 생성하고

print(next(exe_co)) # 넥스트를 실행한다.
print('----------------')
# 출력되는 결과

# started        
# None       # 넥스트함수가 실행 되면서  While True를 실행하고 'yield'까지만 되었다.
# -> ending  #  그리고 Finally를 실행 한다.

# 실행된 함수

# 1. 기존의 함수들이 순서대로 실행되며
# def coroutine_except():
#     print('started')
#     try:

# 2. 제너레이터가 생성되면서 yield까지만 Load 되고 
#         while True:
#             try:
#                 print('?')
#                  yield ############ 여기서 중요한 것은 yield까지만 실행되었다.

# 3. 마지 막으로 finally가 실행되었다.
#    finally:
#         print('-> ending')

print(exe_co.send(10))

# 출력되는 결과

# ??
# received : 10
# ?
# None
# -> ending


# 실행된 함수

# 1. x가 send()로 정의 되고 
#                 x = 
#                 print('??')
# 2. 받았다는 함수로 else문이 실행되고
#             else :
#                 print('received : {}'.format(x))
# 3. 다시 yield로 받을 것이 있는 지 확인하는데 없으므로 None을 확인한다.
                # print('?')
                #     yield

print(exe_co.send(20)) # 위의 send(10)의 과정과 같다.

# 이 제너레이터 함수에 예외를 발생 방법은 무었일까?
# exe_co.throw()를 사용한다.
# 처음에 __doc__만 선언한 클래스Except_를 throw안에 넣어주면
# def coroutine_except(): 내에서  except Except_: 선언한 함수로 호출이 된다.
print('-----------------')
print(exe_co.throw(Except_))

# 출력되는 결과
# Except_ Class that i defined, occurred
# ?
# None
# -> ending

# 실행된 함수
#1. except Except_:을 실행 하고

#2. 까지만 실행한 다음 None을 출력하고
#             try:
#                print('?')
#                yield

#3. finally까지만 출력한다.

# 위에서는 예외만 처리해서 그렇지 실행은 가능하다
print(exe_co.send(100))

# 이 제너레이터 함수에  값을 더 이상 받지 않는 방법은 무었일가?
# close()를 사용하면 된다.
print('------')
print(exe_co.close())

# 출력되는 결과
# -> ending
# None

# 함수 실행
# finally만 실행된다.  

# 이제 제너레이터는 위에서 닫힌 상태이므로 값의 전달이 더이상 되지 않는다.
# print(exe_co.send(200))
# Traceback (most recent call last):
#   File "Day18.py", line 309, in <module>
#     print(exe_co.send(200))
# StopIteration


# return을 사용하는 코루틴예제를 만들어 보겠습니다.

def average_():
    total = 0.0  # next()할때 마다 누산값
    cnt   = 0    # next()실행 횟수
    avg   = None # next()할때 마다 누산값 / next()실행 횟수

    while True:
        print('before')
        term = yield
        print('after')        
        if term is None: # 위와 다르게  None일경우 실행을 하지않고 멈춥니다.
            break

        total += term
        cnt   += 1
        avg   = total / cnt
    return 'avg : {}'.format(avg)

# 제너레이터를 생성하고
avg1 = average_()

# next()로 yield를 준비 시킨 다음에
next(avg1) #before 

# 값을 100씩 집어 넣겟다.
# 추가적으로 term이 실행되고 yield를 준비 시켜놓는다.
avg1.send(100) # after before
avg1.send(100) # after before
avg1.send(100) # after before
# print(avg1.avg)

# None을 의도적으로 넣어서 에러메시지를 발생시켜 함수를 멈추고 return을 반환하게 해 보겠습니다.
try: 
    avg1.send(None)
except Exception as e:
    print(e.value) # avg : 100.0

# 코루틴을 직접 사용해 보겠습니다.
# StopIteration을 자동처리하는 yield from (3.7버전부터 await으로 용어 변경) 을 사용해 보겠습니다.
# 예시는 중첩 코루틴을 사용하겠습니다.

# 그전에 기존에 하던 방식대로 중첩 코루틴을 사용해 보겠습니다.
def co1():
    for i in 'WeExhausted':
        yield i
    for j in range(1,4):
        yield j

c1 = co1()

print(next(c1)) # W
print(next(c1)) # e
print(next(c1))
print(next(c1))
print(next(c1))
print(next(c1))
print(next(c1))
print(next(c1))
print(next(c1))
print(next(c1))
print(next(c1)) # d
print(next(c1)) # 1
print(next(c1)) # 2
print(next(c1)) # 3
# print(next(c1)) # 다음에 호출하면 에러가나온다

# 리스트로 선언하면?
c2 = co1()
#dkfdktj qksghksgksek.
print(list(c2)) # ['W', 'e', 'E', 'x', 'h', 'a', 'u', 's', 't', 'e', 'd', 1, 2, 3]

# 위에까진 기존에 사용하던 방식입니다.
# yield from 뒤에서 정의했던 모든 처리 방식을 알아서 해준다는 의미입니다.
def co2():
    yield from 'WeExhausted'
    yield from range(1,4)
c3 = co2()


print(next(c3)) # W
print(next(c3)) # e
print(next(c3))
print(next(c3))
print(next(c3))
print(next(c3))
print(next(c3))
print(next(c3))
print(next(c3))
print(next(c3))
print(next(c3)) # d
print(next(c3)) # 1
print(next(c3)) # 2
print(next(c3)) # 3

c4 = co2()
print(list(c4))  # ['W', 'e', 'E', 'x', 'h', 'a', 'u', 's', 't', 'e', 'd', 1, 2, 3]

# 서브 코루틴을 선언한다.
# 서브 코루틴은 yield만 사용한다.
def sub_co():
    print('서브 코루틴 시작')
    x = yield 5
    print('received : ', str(x))
    x = yield 10
    print('received : ', str(x))

# 메인 코루틴은 yield from을 사용한다.
# 알아서 흐름제어를 해준다.
# yield from 에서 에러메시지만 처리해주면 에러는 안납니다.
def main_co():
    yield from sub_co()

c5 = main_co()

print(next(c5))
print(c5.send(10)) 
# received :  10
# 10

# print(c5.send(100)) # 일부러 StopIteration 에러 처리를 나게했습니다.
# received :  100





# yield from을 asyncio로 대처해 보기