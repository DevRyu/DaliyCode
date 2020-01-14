def bubble(data):

    for i in range(len(data) -1):
        result = False
        for j in range(len(data) -i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                result = True
        
        if result == False:
            break
    return data
import random


random_list = random.sample(range(100), 50)
print(bubble(random_list))
# [0, 1, 3, 4, 6, 10, 12, 13, 14, 15, 18 ...]