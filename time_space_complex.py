# 시간복잡도 = 시간 
# 공간복잡도 = 메모리 할당량
# 테스트시 외부환경에 따라 달리 시간과 공간이 평가되므로 위의 두가지의 복잡도로 계산
# 시간복잡도가 작다 -> 빠른 알고리즘
# 거듭제곱(Exponentiation)과 로그(반대)
# loga_b = x b를 a로 몇번 나누어야 1이 되는가
# EX) log2_4 = 2 

# 점근 표기법 (Big O notation)
# 소요시간 
# n+1         = O(n)
# 10N_2 + 8N  = O(N_2)
# 10logn + 20 = O(logn)

# n이 별로 크지 않으면 않좋은 알고리즘 써도 상관없음
# 중요한 건 n의 승수가 큰지 안큰지 가 중요하다.

# 인풋리스트 길이 n일대
# O(1) 어떤 n이 와도 1초
# O(n) n에 비례해서 n초
# O(n_2) n의 제곱 n_2초
# O(n_3) n의 세제곱 n_3초

# 컴퓨터가 아무리 좋아도 10000번 이상가면 알고리즘의 시간복잡도에서 벗어나지 못한다.
# 그래서  알고리즘의 시간복잡도를 고려하는 것이 중요하다! 
# 물론 간단하게 생각해서 파이썬의 시간을 내가 측정하고 아는것 도 조금은 필요하지만
# 크게 생각해서 시간복잡도를 계산해서 효율적인 코딩을 하는편이 공수가 좋다.

#       선형 // 이진
# 최고   O(1) | O(1)
# 최악   O(n) | O(logn)
# 항상 최악의 경우를 생각하고 시간복잡도를 부르자
# 선형 O(n)     시간 복잡도
# 이진 O(logn)  시간 복잡도


# 시간 복잡도 & 공간 복잡도 계산 공수가 적다
# 코드 로직 공수가 크다


# 비선형 자료 구조는 꼭짓점(vertex)과 변(edge)으로 이루어져 있습니다. 
# 꼭짓점의 개수 : V
# 변의 개수     : E
# 두 꼭짓점 간 최단 경로찾는 알고리즘 : BFS 알고리즘(시간 복잡도는 O(V+E))

# 코드의 모든 줄은 코드의 모든 줄은 O(1)이 아니다!!!!
# 인풋 크기와 상관 없이 실행 되는 코드만 O(1)
# ex)sorted 함수나 sort 메소드를 사용시 내부적으로 O(nlgn)
# ex)for i in [] 를 사용하면  내부적으로 O(n)의 선형 탐색

# 시간 복잡도는 대개 이 중 하나입니다.

# O(1)
# O(lgn)
# O(n)
# O(nlgn)
# O(n2)
# O(n3)
# O(n4)
# O(2n)
# O(n!)


# O(1)은 인풋의 크기가 소요 시간에 영향이 없다
# O(1) 함수
# def print_first(my_list):
#     print(my_list[0])
# 반복문이 없으면 대체로 O(1)입니다

# O(n)
# 반복문이 있고, 반복되는 횟수가 인풋의 크기와 비례하면 일반적으로 O(n)

# O(n_2) 반복문 내 반복문
# O(n_3) 반복문 내 반복문 내 반복문

# O(log n) 함수
# 2의 거듭제곱을 출력하는 함수
# (이번에는 인풋이 리스트가 아니라 그냥 정수입니다)
# def print_powers_of_two(n):
#     i = 1
#     while i < n:
#         print(i)
#         i = i * 2
# n이  128일때 2*7승

# # 2의 거듭제곱을 출력하는 함수
# # (이번에는 인풋이 리스트가 아니라 그냥 정수입니다)
# def print_powers_of_two(n):
#     i = n
#     while i > 1:
#         print(i)
#         i = i / 2


# O(n2) 은 O(n)과 O(n)이 중첩된 거죠? 같은 논리로, O(nlgn)은 O(n)과 O(lgn)이 겹쳐진 것입니다.
# Case 1
# def print_powers_of_two_repeatedly(n):
#     for i in range(n): # 반복횟수: n에 비례
#         j = 1
#         while j < n: # 반복횟수: lg n에 비례
#             print(i, j)
#             j = j * 2
# 위 코드에서 for문의 반복횟수는 n에 비례하는데, while문의 반복횟수는 lgn에 비례합니다. while문이 for문 안에 중첩되어 있기 때문에 위 코드의 시간 복잡도는 O(nlgn)이라고 할 수 있습니다.

# Case 2
# def print_powers_of_two_repeatedly(n):
#     i = 1
#     while i < n: # 반복횟수: lg n에 비례
#         for j in range(n): # 반복횟수: n에 비례
#             print(i, j)
#         i = i * 2



# 코드없이 알고리즘 평가 하는 팁
# 최악의 경우를 평가하자. 
# 코드가 몇줄인지 보자.

# 공간 복잡도(Space Complexity)는 인풋 크기에 비례해서 
# 알고리즘이 사용하는 메모리 공간을 나타냅니다. 물론 공간 복잡도도 
# 점근 표기법으로 표현할 수 있기 때문에 간편하게 Big-O 표기법을 사용할 수 있습니다.

# O(1)
# def product(a, b, c):
#     result = a * b * c
#     return result
# 파라미터 a, b, c가 차지하는 공간을 제외하면 추가적으로 
# 변수 result가 공간을 차지합니다. result가 차지하는 메모리 공간은 
# 인풋과 무관하기 때문에 함수 product의 공간 복잡도는 O(1)입니다.

# O(n) 
# def get_every_other(my_list):
#     every_other = my_list[::2]
#     return every_other
# 인풋 my_list의 길이를 n이라고 합시다.

# 파라미터 my_list가 차지하는 공간을 제외하면 추가적으로 변수 every_other가 공간

# O(n2)
# def largest_product(my_list):
#     products = []
#     for a in my_list:
#         for b in my_list:
#             products.append(a * b)
    
#     return max(products)
# 인풋 my_list의 길이를 n이라고 합시다.

# 파라미터 my_list가 차지하는 공간을 제외하면 추가적으로 변수 products, a, b가 
# 공간을 차지합니다. 우선 a와 b는 그냥 정수 값을 담기 때문에 O(1)이겠죠? 
# 그렇다면 products가 차지하는 공간은 어떻게 표현할 수 있을까요?

# 리스트 products에는 my_list에서 가능한 모든 조합의 곱이 들어갑니다. 
# 그렇다면 총 n2 개의 값이 들어가겠죠? 따라서 largest_product의 
# 공간 복잡도는 O(n2)
# https://keichee.tistory.com/272
# https://www.codeit.kr/assignments/1419