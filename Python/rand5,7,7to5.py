import sys
import random


def rand5():
    return random.randint(1, 4)

# rand5()함수를 활용한 rand7()만들기
def rand7():
    num = 22
    while num > 21:
        row = rand5()
        col = rand5()
        num = (row-1) * 5 + col
    return num % 7 + 1

print(rand7())
print(rand7())
print(rand7())

# rand7()함수를 활용한 rand5()만들기
def rand7_to_rand5():
    num = 7
    while num >= 5:
        num = rand7()
    return num

# 1이상 5이하의 정수
print(rand7_to_rand5())
print(rand7_to_rand5())
print(rand7_to_rand5())
