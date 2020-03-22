import random 
data_list = random.sample(range(100), 10)

def bubble(data):
    for index1 in range(len(data)):
        swap = 0
        for index2 in range(len(data)- 1 - index1):
            if data[index2] > data[index2+1]:
                data[index2], data[index2+1] = data[index2+1], data[index2]
                swap += 1
        if swap == 0:
            break
    return data
def insert(data):
    for index1 in range(len(data)):
        key = data[index1]
        for index2 in range(index1, 0, -1):
            if key < data[index2 -1]:
                data[index2 -1], data[index2] = data[index2], data[index2-1]
            else:
                break
    return data
def select(data):
    for index1 in range(len(data)-1):
        lowest = index1
        for index2 in range(index1, len(data)):
            if data[lowest] > data[index2]:
                lowest = index2
        data[index1], data_list[lowest] = data[lowest], data[index1]
    return data

def mergesplit(data):
    if len(data) <= 1:
        return data
    medium = len(data)//2
    left = mergesplit(data[:medium])
    right = mergesplit(data[medium:])
    
    return merge(left, right)

def merge(left, right):
    result = list()
    left_idx, right_idx = 0, 0

    # 왼쪽 오른쪽 둘다 데이터 존재
    while len(left) > left_idx and len(right) > right_idx:
        if left[left_idx] > right[right_idx]:
            result.append(right[right_idx])
            right_idx += 1
        else:
            result.append(left[left_idx])
            left_idx += 1
    # 왼쪽만 존재
    while len(left) > left_idx:
        result.append(left[left_idx])
        left_idx += 1
    # 오른쪽만 존재
    while len(right) > right_idx:
        result.append(right[right_idx])
        right_idx += 1
    return result

def quick_sort(data_list):
    if len(data_list) <= 1:
        return data_list
    
    left, right = list(), list()
    pivot = data_list[0]
    
    for index in range(1, len(data_list)):
        if pivot > data_list[index]:
            left.append(data_list[index])
        else:
            right.append(data_list[index])
    return quick_sort(left) + [pivot] + quick_sort(right)


print(bubble(data_list))
print(insert(data_list))
print(select(data_list))
print(mergesplit(data_list))
print(quick_sort(data_list))
