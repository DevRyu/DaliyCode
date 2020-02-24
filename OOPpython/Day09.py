# Chapter 03. Sequence - 01. Advanced List & Tuple - 1

# 파이썬 
# 시퀸스형(순서,순차)에서
# 컨테이너(서로 다른 자료형): tuple , list , collections.deque
# 플랫(하나의 자료형)       : str,bytes,bytearray,array.array, memoryview
# 가변(mutable)   : list, bytearray, array.array, memoryview, deque
# 불변(immutable) : tuple,str,bytes



# 컨테이너에 관련된 파이썬의 기능들을 알아 보자

# 기존에 c나 자바에서의 리스트 값 추가하는 구조의 코드
list_ = []
for i in range(10):
    list_.append(i)
print(list_)

# 리스트 컴프리핸션(List Comprehension) 지능형 리스트라고도 한다.
# 람다함수(익명함수)와 비슷한 구조로 생성되며 리스트내에 for문을 사용한다.
# 구조 : [ 인자(필수)  for문(필수)  조건문(옵션)] 의 형태를 띄우며 싱글톤 객체에 명시한다.
# 단 for문  조건문 뒤에 붙이는 ":" 는 생략한다.
# ex1) 
a = [i for i in range(10)]
print(a) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# ex2)
a = [i for i in range(10) if i%2 == 0]
print(a) # [0, 2, 4, 6, 8]
# ex2-1) 하지만 else 사용시 주의해야할게 있다.
# else가 있으면 이 구조 대로 작성해야 한다. : [ 인자(필수) 조건문(옵션) for문(필수)]
ab = [x if x%2 == 0 else 0 for x in range(10)]
print(ab)

# map, filter,람다 함수로도 for문을 작성 할 수도 있다.
b = list(filter(lambda i : i%2 == 0 , map(int, range(10))))
print(b) # [0, 2, 4, 6, 8]

# 리스트 컴프리 헨션이  map,fiter,람다문 보다 데이터 값이 많을 수록 더 빠르다.

# 디스어셈블의 결과
from dis import dis
# 빈리스트에 for문에서 append()사용 시 
print(dis('''
list_ = []
for i in range(10):
    list_.append(i)
'''))

# ----------------동기적 진행?--------------------
#   2           0 BUILD_LIST               0
#               2 STORE_NAME               0 (list_)

#   3           4 SETUP_LOOP              26 (to 32)
#               6 LOAD_NAME                1 (range)
#               8 LOAD_CONST               0 (10)
#              10 CALL_FUNCTION            1
#              12 GET_ITER
#         >>   14 FOR_ITER                14 (to 30)
#              16 STORE_NAME               2 (i)

#   4          18 LOAD_NAME                0 (list_)
#              20 LOAD_METHOD              3 (append)
#              22 LOAD_NAME                2 (i)
#              24 CALL_METHOD              1
#              26 POP_TOP
#              28 JUMP_ABSOLUTE           14
#         >>   30 POP_BLOCK
#         >>   32 LOAD_CONST               1 (None)
#              34 RETURN_VALUE
# None



# 리스트 컴프리핸션
print(dis('[i for i in range(10) if i%2 == 0]'))
# -------------- 변수 적재,함수 호출과정-----------------
#   1           0 LOAD_CONST               0 (<code object <listcomp> at 0x7f146c1015d0, file "<dis>", line 1>)
#               2 LOAD_CONST               1 ('<listcomp>')
#               4 MAKE_FUNCTION            0
#               6 LOAD_NAME                0 (range)
#               8 LOAD_CONST               2 (10)
#              10 CALL_FUNCTION            1
#              12 GET_ITER
#              14 CALL_FUNCTION            1
#              16 RETURN_VALUE

# ----------- 함수 실행과정-----------------------
# Disassembly of <code object <listcomp> at 0x7f146c1015d0, file "<dis>", line 1>:
#   1           0 BUILD_LIST               0
#               2 LOAD_FAST                0 (.0)
#         >>    4 FOR_ITER                20 (to 26)
#               6 STORE_FAST               1 (i)
#               8 LOAD_FAST                1 (i)
#              10 LOAD_CONST               0 (2)
#              12 BINARY_MODULO
#              14 LOAD_CONST               1 (0)
#              16 COMPARE_OP               2 (==)
#              18 POP_JUMP_IF_FALSE        4
#              20 LOAD_FAST                1 (i)
#              22 LIST_APPEND              2
#              24 JUMP_ABSOLUTE            4
#         >>   26 RETURN_VALUE
# None


print(dis('list(filter(lambda i : i%2 == 0 , map(int, range(10))))'))
# -------------- 변수 적재,함수 호출과정-----------------
#   1           0 LOAD_NAME                0 (list)
#               2 LOAD_NAME                1 (filter)
#               4 LOAD_CONST               0 (<code object <lambda> at 0x7f146c1015d0, file "<dis>", line 1>)
#               6 LOAD_CONST               1 ('<lambda>')
#               8 MAKE_FUNCTION            0
#              10 LOAD_NAME                2 (map)
#              12 LOAD_NAME                3 (int)
#              14 LOAD_NAME                4 (range)
#              16 LOAD_CONST               2 (10)
#              18 CALL_FUNCTION            1
#              20 CALL_FUNCTION            2
#              22 CALL_FUNCTION            2
#              24 CALL_FUNCTION            1
#              26 RETURN_VALUE

# ----------- 함수 실행과정-----------------------
# Disassembly of <code object <lambda> at 0x7f146c1015d0, file "<dis>", line 1>:
#   1           0 LOAD_FAST                0 (i)
#               2 LOAD_CONST               1 (2)
#               4 BINARY_MODULO
#               6 LOAD_CONST               2 (0)
#               8 COMPARE_OP               2 (==)
#              10 RETURN_VALUE

# 사실 여기서 더 정확히 어떤 동작을 하는지에 대해 찾아 보고 싶으나 
# 멋진 개발자로서 갈길이 멀어서 디스어셈블의 정확한 과정에 대한 설명은 잠시 덮어두고 
# 어셈블리어 수업을 들엇던 토대로 개인적인 의견을 적고자 합니다. (틀릴 수도 있습니다.)

# 이것은 개인 의견입니다만
# 변수 적재,함수 호출과정(메모리의 영역)에서는  list comprehension이 더 적은 처리를 하였고
# 함수 실행과정(CPU 연산)에서는 map, filter, lambda 의 과정이 더 단순하였습니다.

# 그래서 위의 두 코드들을 테스트 코드 작성으로 실행 속도만 측정하고 글을 마칠려고 합니다.

# 속도 측정을 테스트 코드로 실행해 보겠습니다.

import timeit

def aa(): 
    SETUP_CODE = ''' 

from __main__ import aa 
'''
      
    TEST_CODE = ''' 
list_ = []
for i in range(10):
    list_.append(i)
'''
    times = timeit.repeat(setup = SETUP_CODE, 
                          stmt = TEST_CODE, 
                          repeat = 3, 
                          number = 10000) 
  
    print('for, append: {}'.format(sum(times) / len(times)))   




def bb(): 
    SETUP_CODE = ''' 

from __main__ import bb 
'''
      
    TEST_CODE = ''' 

b = [i for i in range(10) if i%2 == 0]
'''
    times = timeit.repeat(setup = SETUP_CODE, 
                          stmt = TEST_CODE, 
                          repeat = 3, 
                          number = 10000) 
  
    print('List Comprehension time: {}'.format(sum(times) / len(times)))   


def cc(): 
    SETUP_CODE = ''' 

from __main__ import cc
'''
      
    TEST_CODE = ''' 

c = list(filter(lambda i : i%2 == 0 , map(int, range(10))))
'''
    times = timeit.repeat(setup = SETUP_CODE, 
                          stmt = TEST_CODE, 
                          repeat = 3, 
                          number = 10000) 
  
    print('fliter, map lambda time: {}'.format(sum(times) / len(times)))   


if __name__ == "__main__": 
    aa() # for, append: 0.00838560166660803
    bb() # List Comprehension time: 0.007693430666525576
    cc() # fliter, map lambda time: 0.01972534966656288

# 여러 번 실행한 터라 이미 메모리에서 자주쓰는 코드를적재 시켜놓은 터라 
# 첫번째 for문 사용한 리스트 빠르게 결과 값이 나오는 것 같기도 합니다.

# List Comprehension이 압도적으로 빠릅니다

# 리스트내에 for문을 통한 값 할당시 무조건 지능형 리스트 컴프리헨션이 빠른 것 같습니다.
 