# 파이썬에서 in 연산자 (연결 연산자)는 선형 탐색에서 어떤 힘을 발휘하는가?

# Insight
# 파이썬에서의 in연산자(연결연산자)는 이미 sequence안에서 선형 탐색을 해주는 기능이 있다.
# 파이썬스러운 코딩은 in을 활용해서 선형탐색 시간을 단축하는 것이다.
# 그래서 for문(반복문)을 쓰지 않고 if문(분기문) 하나로 문제를 해결할 수 있다.
# pep8스타일을 지향하는 것 특히 간결하게 코딩을 하는 것이 성능 향상의 지름길이다.
# 같은 기능 서로 조금식 다른 방법의 함수를 코딩하면서 어떤것이 더 빠른가 생각해 보게 되었다.

# 선형 탐색이란 리스트의 처음부터 끝까지 순서대로 하나씩 탐색을 진행하는 알고리즘입니다.
# 선형 탐색 (for문 사용과 사용하지 않는 예시)어떤 원소가 리스트 안에 포함되어 있는지 확인합니다.
# 결과값은 해당 리스트의 인덱스 번호를 return하는 함수입니다.

# 3가지 여러 풀이를 실행하면서 어떤 방법이 왜 빠른지에 대해 생각하게 된 시간이 되었습니다.

import timeit # 시간 측정


list_ = [1, 7, 15, 2, 6, 3, 4, 5, 7, 11]
# 1.기본적인 for문 형태 range(len()), 반복,분기문
def linear_search(element, some_list):
    for i in range(len(some_list)):
        if  element == some_list[i]:
            return i
        else:  None

start = timeit.default_timer()
print(linear_search(2, list_))
print(linear_search(0, list_))
print(linear_search(5, list_))
print(linear_search(3, list_))
print(linear_search(11, list_))

# 3
# None
# 7
# 5
# 9

stop = timeit.default_timer()
print(stop - start) # 6.075999954191502e-05


# 2.enumerate() 사용, 반복,분기문
def linear_search2(element, some_list):
    for i,j in enumerate(some_list,0):
        if  element == j:
            return i
        else: None 

start2 = timeit.default_timer()
print(linear_search2(2, list_))
print(linear_search2(0, list_))
print(linear_search2(5, list_))
print(linear_search2(3, list_))
print(linear_search2(11, list_))

# 3
# None
# 7
# 5
# 9

stop2 = timeit.default_timer()
print(stop2 - start2) # 3.815099989878945e-05

# 3.분기문만 사용 (in, index())  
def linear_search3(element, some_list):
    if  element in some_list:
        return some_list.index(element)
    else: None 

start3 = timeit.default_timer()
print(linear_search3(2, list_))
print(linear_search3(0, list_))
print(linear_search3(5, list_))
print(linear_search3(3, list_))
print(linear_search3(11, list_))

# 3
# None
# 7
# 5
# 9

stop3 = timeit.default_timer() 
print(stop3 - start3) # 3.383700004633283e-05
 
# 반복, 분기 둘다 포함하는 함수 보다(1,2번)
# 3번째 2번째는 비슷하지만 3번째가 좀더 빨랏고 첫번째는 조금 더 느렸습니다..
# 3번째와 2번째를 비교 하는데 python interpreter I/O가 간접적으로 영향을 끼쳐서 정확한 결과가 아니라고 판단하고
# 조금 더 정확한 측정을 위해 timeit.timeit을 사용하며 테스트 코드를 짜기로 했습니다.


def linear_time(): 
    SETUP_CODE = ''' 

from __main__ import linear_search 
'''
      
    TEST_CODE = ''' 

element    =  11
some_list  = [1, 7, 15, 2, 6, 3, 4, 5, 7, 11]
linear_search(element, some_list) 
'''
    times = timeit.repeat(setup = SETUP_CODE, 
                          stmt = TEST_CODE, 
                          repeat = 3, 
                          number = 10000) 
  
    print('Linear search time: {}'.format(sum(times) / len(times)))   


def linear_time2(): 
    SETUP_CODE = ''' 

from __main__ import linear_search2
'''
      
    TEST_CODE = ''' 

element    =  11
some_list  = [1, 7, 15, 2, 6, 3, 4, 5, 7, 11]
linear_search2(element, some_list) 
'''
    times = timeit.repeat(setup = SETUP_CODE, 
                          stmt = TEST_CODE, 
                          repeat = 3, 
                          number = 10000) 
  
    print('Linear search2 time: {}'.format(sum(times) / len(times)))   

def linear_time3(): 
    SETUP_CODE = ''' 

from __main__ import linear_search3 
'''
      
    TEST_CODE = ''' 

element    =  11
some_list  = [1, 7, 15, 2, 6, 3, 4, 5, 7, 11]
linear_search3(element, some_list) 
'''
    times = timeit.repeat(setup = SETUP_CODE, 
                          stmt = TEST_CODE, 
                          repeat = 3, 
                          number = 10000) 
  
    print('Linear search3 time: {}'.format(sum(times) / len(times)))   


if __name__ == "__main__": 
    linear_time()  # Linear search time: 0.00626433133311366
    linear_time2() # Linear search2 time: 0.004681959333538543
    linear_time3() # Linear search3 time: 0.0035465979999571573

# 위의 예상대로 
# 3번째가 가장 빨랏고 
# 2번재가 그 다음이고 
# 1번째가 가장 느렸습니다. 
# 코드 간결성을 유지 하는 습관의 중요성을 알게되었습니다.