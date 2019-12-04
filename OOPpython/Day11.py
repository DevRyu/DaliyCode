# 파이썬 함수의 특징
# 일급 함수(일급 객체)


# 파이썬 함수 특징
# 런타임 초기화, 변수등에 할당 가능(데코레이터, 클로저), 함수 인수 전달 가능(ex) 제약조건 len=10 등), 함수 결과로 반환 가능

# 클래스와 함수간의 차이는 무엇인가? 라고 물으면 쉽게 답 할수 있을까?
# 구조적 차이는 쉽게 설명이 가능 하다.
# 함수는 행위만을 가지며 클래스는 속성과 행위를 가진다.  
# 그렇다면 세부적으로 파이썬에서는 이 둘 사이에 기능적인 차이는 무엇인가?
# 그 질문은 던지기 전에 파이썬의 자료들은 모두 객체라고 저번에 명시했엇다.

# 함수는 객체인가?
#  예제
def factorial(n):
    '''
    factorial function
    n : int
    '''
    if n == 1:
        return 1
    return n * factorial(n-1)


class F:
    pass

# 함수든 클래스든 모두 객체이다.
print(type(factorial), type(F)) #<class 'function'> <class 'type'>

# 그렇다면 파이썬에서 함수와 클래스가 가지는 내부적 기능의 차이는 어떤 것 일까?

# 클래스에 없는 함수만의 고유한 특징은 아래이다.
# {'__annotations__', '__defaults__', '__qualname__', '__call__', '__kwdefaults__', '__name__', '__globals__', '__get__', '__code__', '__closure__'}
print(set(sorted(dir(factorial))) - set(sorted(dir(F)))) 

print()

# 함수에는 없는 클래스 만의 특징은 아래이다.
 # {'__weakref__'}
print(set(sorted(dir(F))) - set(sorted(dir(factorial))))


# 1. 변수에게 함수 할당하기

f1_func = factorial(5) # return이 int여서 함수가 아닌 정수
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


# 다시 factorial함수를 할당학자

f5_func = factorial
# 할당된 변수를 map함수를 사용해서 for문과 같이 돌릴 수 있다.

print(list(map(f5_func, range(1,6))))



# 함수 인수를 전달하고 함수로 결과를 반환하는 함수를 고위 함수라고 한다 (Higer Order Function)

# 함수안의 함수를 사용해보자
                                    # 홀수인 1,3,5 인자인 함수만 실애하였다.
print(list(map(f5_func, filter(lambda x : x % 2, range(1,6)))))
print([f5_func(i) for i in range(1, 6) if i % 2])

from dis import dis

# 위의 함수를 비교해보자
print(dis.__doc__)
print(dir(dis))
print('-------------------------------------------------------------')
print(dis('list(map(f5_func, filter(lambda x : x % 2, range(1,6))))'))
print(list(map(f5_func, filter(lambda x : x % 2, range(1,6)))))
print('-------------------------------------------------------------')
print(dis('[f5_func(i) for i in range(1, 6) if i % 2]'))
print('-------------------------------------------------------------')

# reduce() 함수 개념

from functools import reduce
# 오퍼레이터의 더하기 기능을 가져온다.
from operator  import add

# reduce함수는 원소들을 중첩(누적)하여 하나로 만드는 과정 왼쪽으로부터 오른쪽까지의 single values를 합치는것입니다.
# 함수, iter한 자료형을 파라미터로 받습니다.

print(reduce(add, range(1,11))) # (((1+2)+3)+4)......10

# 익명함수 (람다)
# 가급적 주석, 함수
# 가독성을 위해 일반 함수 형태로 리펙토링 권장

print(reduce(lamda i,j : i + j , range1,11))

# Callable : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인

