# ‘이진 탐색(Binary Search)’ 알고리즘은 분할과 정복을 사용합니다.. 
# 이진 탐색 알고리즘은 정렬된 리스트를 전제로 합니다. 

# 처음에 푼 방법 
# for loop을 사용할려고 하니 파이썬의 for loop syntex의 in연산자 때문에 
# 재귀함수를 사용해야 할 것 같았다.
# 값은 재대로 리턴을 하나... 인덱스 키값을 유지할려면 함수밖에 리턴을 하고 
# 리턴한 값을 전역scope에서 원래 인덱스와 비교를 해야 했다 라고 생각했다
# 원하는 요구사항은 함수 내에서 해결을 해야하는 부분이였고 
# 인터넷의 예제들은 조금 더 간단하게 while문과 if문만으로 해결을 하는 것 뿐이 였다.
# 일단 아쉬운대로 값만을 리턴하던지 값이 없으면 None을 리턴하는 함수를 만들었다.

# 값이 있으면 값을 return하는 로직 부분
def binary_search(element, some_list):

    half_length = round(len(some_list)/2)
    start_index = 0 
    last_index  = len(some_list) - 1

    if element == some_list[half_length]:
        return some_list[half_length]

    elif half_length == 0:
        return None 

    elif element < some_list[half_length]:           
        return binary_search(element, some_list[:half_length])

    elif element > some_list[half_length]:              
        return binary_search(element, some_list[half_length:])
        
# print(binary_search(2, [2, 3, 5, 7, 11]))
# print(binary_search(0, [2, 3, 5, 7, 11]))
# print(binary_search(5, [2, 3, 5, 7, 11]))
# print(binary_search(3, [2, 3, 5, 7, 11]))
# print(binary_search(11, [2, 3, 5, 7, 11]))


# 다른 언어에서도 이런건 지 확인을 하던 찰나 자바에서 for문 예제가 있어서 리펙토링 해보았다.
# for문을 사용하며 원래 리스트의 인덱스 번호를 리턴하는 방법


def binary_search2(element, some_list):

    start_index = 0 
    last_index  = len(some_list) - 1

    for i in range(len(some_list)):
        half_length = round(last_index - start_index /2)

        if element == some_list[i]:
            return some_list.index(some_list[i])

        elif element < some_list[half_length]:           
            last_index = start_index + 1

        else :              
            start_index = last_index + 1

    return None 

# print(binary_search2(2, [2, 3, 5, 7, 11]))
# print(binary_search2(0, [2, 3, 5, 7, 11]))
# print(binary_search2(5, [2, 3, 5, 7, 11]))
# print(binary_search2(3, [2, 3, 5, 7, 11]))
# print(binary_search2(11, [2, 3, 5, 7, 11]))

# 마지막으로 while문으로 구현 해 보았다.

def binary_search3(element, some_list):

    start_index = 0 
    end_index   = len(some_list) - 1

    while start_index <= end_index:
        # print("start",start_index)
        # print("end",end_index)
        midpoint = (start_index + end_index) // 2

        # print("mid",midpoint)
        if some_list[midpoint] == element:
            return midpoint
        elif element < some_list[midpoint]:
            end_index = midpoint - 1
        else:
            start_index = midpoint + 1

print(binary_search3(2, [2, 3, 5, 7, 11]))
print(binary_search3(0, [2, 3, 5, 7, 11]))
print(binary_search3(5, [2, 3, 5, 7, 11]))
print(binary_search3(3, [2, 3, 5, 7, 11]))
print(binary_search3(11, [2, 3, 5, 7, 11]))


def binary_search3(element, some_list):

    start_index = 0 
    end_index   = len(some_list) - 1

    while start_index <= end_index:
        # print("start",start_index)
        # print("end",end_index)
        midpoint = (start_index + end_index) // 2

        # print("mid",midpoint)
        if some_list[midpoint] == element:
            return midpoint
        elif element < some_list[midpoint]:
            end_index = midpoint - 1
        else:
            start_index = midpoint + 1

print(binary_search3(2, [2, 2, 3, 5, 7, 11]))
print(binary_search3(0, [2, 3, 3, 5, 7, 11]))
print(binary_search3(5, [2, 3, 5, 7, 11]))
print(binary_search3(3, [2, 3, 5, 7, 11]))
print(binary_search3(11, [2, 3, 5, 7, 11]))
