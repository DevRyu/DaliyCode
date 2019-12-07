# 6-1

# 파이썬에서 쓰래드, 태스크, 프로세스를 사용해서 동시적으로 작업들을 처리한다.
# https://ingorae.tistory.com/473
# 쓰레드(thread)    :
# 태스크(task)      :
# 프로세스(process) :
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






# 매직메서드 내장 함수 비교
# iter(a)를 쓰는 도중에 이렇게 파이썬에서 기본적으로 제공하는 메서드를
# 매직메서드(던더)를 직접 불러와서 실행하면 되는지 탐구해 보았다.
# (이미 될거라고 가정은 했지만)
# 결론적으로 된다!

#예를 들어보자
# 2,3을 b,c에 할당 한 후 + 연산자를 사용해보자
b, c =  2, 3

# https://www.python-course.eu/python3_magic_methods.php 참고
print(b+c) # 5
print(b.__add__(c)) # 5 
# 값의 경우 결론적으로 같았다 

# 한가지 더 궁금한 것은 + 와 __add__ 메서드 자체가 같은지 비교하는 것이였다.

# dir내의 사용 가능한 내장 메서드는 같았다
print(set(sorted(dir(b.__add__(c)))) == set(sorted(dir(b+c)))) # True

# 그러나 두 식의 계산과정에서  어셈블 과정에서는 약간의 차이가 있엇다.
# 디스어셈블러를 켜보자
from dis import dis

# BINARY_ADD라는 파이썬의 기능을 바로 사용하여 값을 리턴하였고 
print(dis('b + c'))
#   1           0 LOAD_NAME                0 (b)
#               2 LOAD_NAME                1 (c)
#               4 BINARY_ADD
#               6 RETURN_VALUE
# None


# LOAD_METHOD를 적재하고 함수를 호출하는 과정이 달랐다. 
# 매직 매서드를 사용한 것이니 당연히 과정이 더 필요하다
print(dis('b.__add__(c)'))
#   1           0 LOAD_NAME                0 (b)
#               2 LOAD_METHOD              1 (__add__)
#               4 LOAD_NAME                2 (c)
#               6 CALL_METHOD              1
#               8 RETURN_VALUE
# None

# 이로써 파이썬 코드를 직관적으로 명시할때(지금처럼 함수 호출이 필요 없는 경우)와
# 반대로 직관적으로 보이지만 클래스에 직접접근해서 값을 고치는 비효율적인 경우를 조금은 구별 할 수 있게 되었다.
# 다시 말해 직관적으로 프로그래밍을 하되 예외 사항에 대해서 인지하고 조금 더 성능 좋은 프로그래밍을 할수 있게 되었다.

# 또한 파이썬이 정말 내외부적으로 직관적으로 어떠한 프로그래밍이 더 유용하게 설계 되었 다는 것을 다시 한번 깨닫게 되었다.
# 함수를 불러서 쓰는 것과 binary한 + 연산자로 바로 계산하는 것을 눈에 더 잘띄게 보여졌다.
# 이로서 파이썬에서 + 연산자에서 내부에서 돌아가는 매직메서드를 알아 보았다.








# 흐름제어(control flow), 병행처리(concurrency)

# 파이썬의 제너레이터 (발생자)

# 파이썬의 반복형 종류 : for, collections, string, list, dict, set, tuple, unpacking, *args
# 위의 자료형이 반복이 가능한 이유? => iter()함수를 상위 추상클래스에서 내부적으로 호출을 하기 떄문이다. 

# 반복형 객체 내부적으로 iterator 함수, 제너레이터 동작 원리, yield from 사용하기

# 저도 글을 쓰면서 가끔 헷갈리는 것이지만 클래스(class), 인스턴스, 객체(object)에 대해 제 나름대로의 정의를 해보겠습니다.
# 클래스 : 파이썬의 모든 자료형의 의미도 있고, class A():라는 속성과 행위를 담는 클래스라는 의미도 있습니다. (보통 설계도라고 합니다.)
#  - 전자의 설명이 맞다면 Java와 같이 파이썬도 우리 눈에 보이지 않지만 전역 Scope가 class 로 되어 있고 후자는 내부에 작은 파이의 class를 선언하는 것과 같다고 생각합니다.
# 인스턴스 : 클래스를 객체로 취급하는 것을 클래스의 인스턴스화 한다고 합니다. 인스턴스도 객체 내에 포함이 되는 개념입니다.
# 객체 : 메모리에 존재하는 개별 데이터를 가리키는 개념이라고 합니다. 변수(객체의 이름)인 것은 들은 모두 객체로 취급 할 수 있습니다.


# 이터레이터 예시 
# 이터레이터(반복자) : 값을 차례대로 꺼낼 수 있는 객체(변수))입니다.
# 연속된 숫자를 미리 만들면 숫자가 적을 때는 상관 없지만 많을 때는 메모리를 많이 사용한다.
# 그래서 파이썬에서는 이터레이터만 생성하고 생성된 값이 필요할 때만 값을 만드는데 이러한 방식을 지연 평가라고 한다.(lazy evaluation)

a = '1234567'

# 값을 차례대로 꺼낼수 있다.
for i in a:
    print(i)

# 이터를 선언후
it = iter(a)

# while문에서 반복을 한다.
while True:
    try:
        print(next(it))

    # 브레이크문이 없으면 무한반복    
    except StopIteration:
        break


# it변수가 이터 속성을 가지고 있는지 확인해 보자.
from collections import abc

# hasattr() 이터 속성을 가지고 있는지 확인 하는 함수
print(hasattr(it, '__iter__')) # True값이 출력 된다.

# isinstance() 클래스의 인스턴스인지 확인하는 함수
# 여기서는 it = iter(a)가 된 것을 확인
print(isinstance(it, abc.Iterable)) # True값이 출력 된다. 

# iter의 특징인 next() 함수 만들어서 클래스 만들기
# 아래에서 설명 드리겠지만 Generator라는 것을 사용하기 위해 Iterater의 개념을 먼저 잡겠습니다.
# (마치 비트켄슈타인으 사다리 이론 같군요!)
# 파이썬 시퀀스 프로토콜에서 상속을 안받으면 전에 봤듯이 파이썬엔진에서 알아서 상속해줌
class IterableWork:
    def __init__(self, text):
        print('__init__ was called')
        self._idx   = 0
        self._text  = text.split(' ')

    # 넥스트함수 오버라이딩 정의
    def __next__(self):
        # next함수 실행시 return할 word를 값과 인덱스를 저장
        try:
            print('__next__ was called')
            word =  self._text[self._idx]

        except IndexError:
            print('__next__ was called')
            raise StopIteration('finished') 

        # 한번 실행할때마다 인덱스 값 증가
        self._idx += 1
        return word

    # 이터 함수도 오버라이딩 정의
    def __iter__(self):
        return self
    
    def __repr__(self):
        print('__repr__ was called')
        return 'data(%s)' % (self._text)



result = IterableWork('ah ya oh yo eu wi')

# 그냥 호출하면 전체 데이터를 보여준다.
print(result) # __init__ was called __repr__ was called //  data(['ah', 'ya', 'oh', 'yo', 'eu', 'wi'])

# next(이터러블한 객체)는 처음부터 순차적으로 아이템(객체)을 하나씩 뽑아서 리턴한다. 
# 바로 def __next__ 만 호출된다.
print(next(result)) # __next__ was called // ah
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))  # __next__ was called // wi
# print(next(result))  # StopIteration: finished이 출력됨

# 위의 클래스를 응용해 제너레이터식으로 표현한다.
# 제너레이터는 이터랭터를 생성해주는 함수입니다.
# 이터레이터는 클래스에 __iter__, __next__ 또는 __getitem__ 메서드를 구현을 해야지 사용이가능합니다.
# 하지만 제너레이터는 yield라는 키워드만 있으면 정의하는 클래스가 간단해집니다.
# 제너레이터는 발생자라고 부릅니다.
# 함수안에 yield를 하용하면 함수는 제너레이터가 됩니다. 이유는 제너레이터는 __next__사용시 
# 함수안의 yield까지 코드를 실행 후 yield에서 값을 발생(generate)시킵니다.
# yield 뒤에는 값(변수) 를 지정합니다. 

# 제너레이터 패턴을 사용해야 하는 이유 
# 1. 지능형 리스트, 딕셔너리, 집합같은 큰 자료형들은 특징이 데이터 셋이 크기카 클 경우  메모리 사용량이 큽니다.(100만 단위로 생각해 보세요)
# -> 사용하지 않는(즉 next로 호출 될 일이 없는 뒤에 있는 자료들은) 데이터는 메모리에 적재하지 않습니다.
# -> 즉 필요한 데이터만 메모리에 올리므로 제너레이터로 완화가 됩니다.
# 2. 1에서 본 이유로 테스크 단위 실행이 가능 코루틴(Coroutine) 구현에 매우 중요합니다.
# 3. 딕셔너리, 리스트들은 한 번 호출 할 때 마다 하나의 값만 리턴합니다.-> 실제로 작은 메모리양만 필요하다는 현실적인 이유도 있습니다. 

class GenerableWork:
    def __init__(self, text):
        print('__init__ was called')
        self._text  = text.split(' ')

    # 이터 함수도 오버라이딩 정의
    def __iter__(self):
        print('__iter__ was called')
        for word in self._text:
            yield word
        return
    
    def __repr__(self):
        print('__repr__ was called')
        return 'data(%s)' % (self._text)

result = GenerableWork('ah ya oh yo eu wi')
print(dir(result)) # '__iter__' 속성을 가지고 있어서 
gt_result = iter(result) #1. 직접 변환을 해줘도 되고

print(next(gt_result)) #  ah
print(next(gt_result))
print(next(gt_result))
print(next(gt_result))
print(next(gt_result))
print(next(gt_result))  #  wi
# print(next(gt_result))  # StopIteration

#2. result.__iter__().__next__() 메서드 체이닝 형태로 하셔도 됩니다.
print(result.__iter__().__next__()) # ah
print(result.__iter__().__next__())
print(result.__iter__().__next__())
print(result.__iter__().__next__())
print(result.__iter__().__next__())
print(result.__iter__().__next__()) # wi
# print(result.__iter__().__next__()) # StopIteration

# 위의 방법 중 증명은 안하겠지만 더 효율적인것은 1번째라고 생각이 듭니다.
# 2번째 방법은 항상 iter를 출력하는 건 마다 Load후 Call을 하는 반면
# 1번째 방법은 한번에 변환후 접근하능 형식이 한번만 __next__로 call하면 됩니다.

# 이터레이터 vs 제너레이터 차이
# 이터레이터는 __next__ 메서드 안에서 직접 return으로 값을 반환합니다. 
# 제너레이터는 yield에 지정한 값이 __next__ 메서드(next 함수)의 반환값으로 나옵니다. 
# 이터레이터는 raise로 StopIteration 예외를 직접 발생시킵니다.
# 제너레이터는 함수의 끝까지 도달하면 StopIteration 예외가 자동으로 발생합니다




# 제너레이터는 함수로써 실제로 활용이 많이 됨으로 함수로 호출해 보겠습니다.

def generator1():
    print('start')
    yield 'A'
    print('generating')
    yield 'B'
    print('end')

# 방법1. __next__() 쓰기
# yield가 함수안에 있으므로 자동으로 변수 지정시 제너레이터라고 인식합니다
g1 = generator1()

print(g1.__next__())
print(g1.__next__())

# 방법2.iter()로 재지정후  next()쓰기
g2 = iter(generator1())
print(next(g2))
print(next(g2))

# 이건 뭐가 더 효울적인지 감이 안와서 어셈블해보겠습니다.
print(dis('g1.__next__()'))
#   1           0 LOAD_NAME                0 (g1)
#               2 LOAD_METHOD              1 (__next__)
#               4 CALL_METHOD              0
#               6 RETURN_VALUE
# None
print(dis('next(g2)'))
#   1           0 LOAD_NAME                0 (next)
#               2 LOAD_NAME                1 (g2)
#               4 CALL_FUNCTION            1
#               6 RETURN_VALUE
# None

# 감이 안온 게 같아서 그런걸까요?
# 함수를 1번 적재하는가 2번 적재하는가 차이는 없는거 같습니다.
# 하지만 저라면 후자로 좀더 명시적으로 감싸는 편이 좋을거 같습니다.

# 6-03 1:55