import sys
import random


def rand5():
    return random.randint(1, 4)

def rand7():
    num = sys.maxsize
    while num > 21:
        row = rand5()
        col = rand5()
        num = (row-1) * 5 + col
    return num % 7 + 1

print(rand7())