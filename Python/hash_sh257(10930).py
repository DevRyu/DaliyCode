# https://www.acmicpc.net/problem/10930
# SHA-256
# 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# 1 초	256 MB	586	445	421	76.965%
# 문제
# 문자열 S가 주어졌을 때, SHA-256 해시값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 문자열 S가 주어진다. S는 알파벳 대문자와 소문자, 그리고 숫자로만 이루어져 있으며, 길이는 최대 50이다.

# 출력
# 첫째 줄에 S의 SHA-256 해시값을 출력한다.

# 예제 입력 1 
# Baekjoon
# 예제 출력 1 
# 9944e1862efbb2a4e2486392dc6701896416b251eccdecb8332deb7f4cf2a857
n = int(input())
array = set(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))
for i in x:
    if i not in array:
        print('0')
    else:
        print('1')