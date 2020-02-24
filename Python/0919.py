# a = input()

# for i in a:
#     if i == 'A':
#         print("best!!!")
#     elif i == 'B':
#         print("good!!")
#     elif i == 'C':
#         print("run!")
#     elif i == 'D':
#         print("slowly~")
#     else:
#         print("what?")


# a = list(input())
# print(str(a))
# for i in range(len(a)):
#     if '0' in a[i]:
#         break
#     print(a[i])


# import string
# a = string.ascii_lowercase[:]
# b = input()
# for i in range(len(a)):
#     print(a[i])
#     if a[i] == b:
#         break

# a = int(input())
# b = 0
# for i in range(99):
#     b += i+1
#     if a == b:
#         print(i+1)
#         break
#     elif a < b:
#         print(i+1)
#         break

# a = int(input(), 16)
# for i in range(1, 16):
#     b = a*i
#     print("%X*%X=%X" % (a, i, b))
# # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# # print(내에 문자열""과 정수또는 변수 같이 못씀 포메팅해줘야함)

# 라인 19년 마지막 문제
# a, b = input().split(" ")
# matrix = [[0] * (N+1)]
# print(a, b)
# c = 0
# def k(a,b):
#     for i in range(1,20000):
#         if b == a :
#             return c
#             #0초 일때 또는 같아질때의 초
#         c += 1
#         a += c
#         elif a > b :

#         return c

# 0+1 =1
# 1+1 =2
# 2+1 =3
# 1
# 1+2
# 1+2+3

# 재귀 알고리즘
# n = int(input())
# a, b = 0, 1
# while n > 0:
#     a, b = b, a+b
#     n -= 1
# print(a)

# 5
# 1,1
# 4
# 1,2
# 3
# 2,3
# 2
# 3,5
# 1
# 5,8

# 5


# multiples of 3 and 5

# n = int(input())
# # 3 6 9 12 15 18 21 24 27 30
# # 30
# # 15의 배수는 하나로 통합하자 겹치니
# a = 3
# b = n // a
# # n이 32이면 10개 나오지?
# c = 0
# for i in range(b):
#     c += a
#     print(a)
#     a += 3
# d = 5
# e = n // 5
# f = 0
# for i in range(e):
#     if (d % 15 == 0):
#         print(d)
#         d += 5
#         continue
#     else:
#         print(d)
#         f += d
#         d += 5
# print(c+f)

# # 또는 Set
# set3 = set(range(3, 21, 3))
# set5 = set(range(5, 21, 5))
# print(sum(set3 | set5))

# # 또는 한줄로
# # sum(list([x for x in range(1000) if x%3==0 or x%5==0]))


# a, b = map(int, input().strip().split(' '))
# d = []
# for i in range(a):
#     d.append(int(input()))
# for i in range(b):
#     c = [[]]*b
#     c[i][0] = d.pop(i)
# print(c)
# for i in range(a-b):
#     if c[i][0] > c[i+1][0]:
#         c[i+1][0] = d[i+2].add()
#     elif c[i+1][0] > c[i][0]:
#         c[i][0] = d[i+2].add()
# print(a, b)
# print(d)


# import itertools
# a, b, c = map(int, input().strip().split(' '))
# g = int(input())
# e = []
# for i in range(1):
#     e.append(a)
#     e.append(b)
#     e.append(c)
#     e = sorted(e)
# f = []
# y = itertools.permutations(e, len(e))
# for i in y:
#     f.append(list(i))
# k = f[g-1]
# k = "".join(map(str, k))
# print(k)


# a = int(input())
# for i in range(1):
#     S = list(map(int, input().split(" ")))
# count = S.count(1)
# K = []
# for i in range(len(S)):
#     if 1 == S[i]:
#         K.append(i+1)
# pairs = list(zip(K[0:], K[1:]))
# pairs.sort(key=lambda x: x[1] - x[0])
# c = list(pairs[0])
# d = c[1]-c[0]
# print(d)

# a = int(input())
# d = set()
# for i in range(a):
#     d[i] = int(input())
# x = range(1, 10)
# print(x)


# a = int(input())
# b = [[int(range(a, b)) for x in input().split(" ")]for y in range(a)]
# print(b)
# for i in range(len(a)):
#     for j in range(2):
#         range(a, b)
# c = set(b)
# # c.intersection(y)
# print(c)
