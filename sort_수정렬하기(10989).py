# https://www.acmicpc.net/problem/10989

# 수 정렬하기 3
# 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# 3 초 (하단 참고)	8 MB (하단 참고)	55754	11887	8858	22.871%
# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# 예제 입력 1 
# 10
# 5
# 2
# 3
# 1
# 4
# 2
# 3
# 5
# 1
# 7
# 예제 출력 1 
# 1
# 1
# 2
# 2
# 3
# 3
# 4
# 5
# 5
# 7
# 수의 범위가 1~10000임으로 계수정렬 알고리즘을 사용할수 있다
# 수의 종류별 빈도수로 정렬할 수 있다.
# 데이터 입력하는 개수가 많을때 sys.stdin.readline()이 input()보다 빠르다.

def solution(N,data):
    data_dict = {}
    for i in range(10001):
        data_dict.update({i:0})
    result = []
    for i in data:
        if data_dict[i] != 0:
            data_dict[i] += 1
        else:
            data_dict.update({i:1})
    for i in range(10001):
        if data_dict[i] != 0:
            print(data_dict[i])
            for j in range(data_dict[i]):
                result.append(i)
    return result

print(solution(10,[5,2,3,1,4,2,3,5,1,7]))
#[1, 1, 2, 2, 3, 3, 4, 5, 5, 7]