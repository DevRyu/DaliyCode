a = int(input())
n = {}
for i in range(a):
    b, c = input().split(" ")
    print(b)
    print(c)
print(n)

# 파이썬 정렬 2가지 list.sort()와
# sorted(list, key=속성으로 함수를 넣어주면 함수를 기준으로 정렬됨)
# lambda 인자 : 리턴값
# 첫번째원소만 정렬되면 나머지 원소또한 정렬이됨 ( stable한 속성)
