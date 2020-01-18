# 선택 정럴
# 처음수를 기준으로(pivot) 작은 수를 찾은 다음 맨앞으로 보낸다
# 이미 정렬한 값은 건들지 아니하고 위의 과정을 반복한다
# pivot이 인덱스 번호로 존재함

def selection(data):
    # 0부터 길이의 n-1까지
    for i in range(len(data) - 1):
        lowest = i # 하나하나씩 기준 인덱스넘버

        # 첫번째 리스트 칸부터 정렬하면서 점점 줄어들며 비교반복 
        for j in range(i + 1,len(data)):
            # 혹시 인덱스 기준값이 작다면 변경한다.
            if data[lowest] > data[j]:
                lowest = j
        # 0번째부터 n-1번째 까지 위치를 바꾸어 준다
        data[lowest], data[i] = data[i], data[lowest]
    
    return data

import random
data_list = random.sample(range(100), 10)
print(selection(data_list))