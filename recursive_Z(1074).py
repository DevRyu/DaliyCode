# https://www.acmicpc.net/problem/1074
# Z
# 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# 2 초	512 MB	14307	6035	4218	41.854%
# 문제
# 한수는 2차원 배열 (항상 2^N * 2^N 크기이다)을 Z모양으로 탐색하려고 한다. 예를 들어, 2*2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.



# 만약, 2차원 배열의 크기가 2^N * 2^N라서 왼쪽 위에 있는 칸이 하나가 아니라면, 배열을 4등분 한 후에 (크기가 같은 2^(N-1)로) 재귀적으로 순서대로 방문한다.

# 다음 예는 2^2 * 2^2 크기의 배열을 방문한 순서이다.



# N이 주어졌을 때, (r, c)를 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.

# 다음 그림은 N=3일 때의 예이다.



# 입력
# 첫째 줄에 N r c가 주어진다. N은 15보다 작거나 같은 자연수이고, r과 c는 0보다 크거나 같고, 2^N-1보다 작거나 같은 정수이다

# 출력
# 첫째 줄에 문제의 정답을 출력한다.

# 예제 입력 1 
# 2 3 1
# 예제 출력 1 
# 11
# 예제 입력 2 
# 3 7 7
# 예제 출력 2 
# 63

count = 0
X, Y = 5,1

def solution(n, x, y):
    global count
    if n == 2:
        if x == X and y == Y:
            return count
        count += 1
        if x == X and y+1 == Y:
            return count
        count += 1
        if x+1 == X and y == Y:
            return count
        count += 1
        if x+1 == X and y+1 == Y:
            return count
        count += 1
        return None
    if solution(n/2, x, y):
        return count
    elif solution(n/2, x, y + n / 2):
        return count
    elif solution(n/2, x + n / 2 , y):
        return count
    elif solution(n/2, x + n / 2, y + n / 2):
        return count

print(solution(2**3,0,0))
# 35