# https://www.acmicpc.net/problem/2920
# 문제
# 다장조는 c d e f g a b C, 총 8개 음으로 이루어져있다. 이 문제에서 8개 음은 다음과 같이 숫자로 바꾸어 표현한다. c는 1로, d는 2로, ..., C를 8로 바꾼다.

# 1부터 8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending, 둘 다 아니라면 mixed 이다.

# 연주한 순서가 주어졌을 때, 이것이 ascending인지, descending인지, 아니면 mixed인지 판별하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 8개 숫자가 주어진다. 이 숫자는 문제 설명에서 설명한 음이며, 1부터 8까지 숫자가 한 번씩 등장한다.

# 출력
# 첫째 줄에 ascending, descending, mixed 중 하나를 출력한다.

# 예제 입력 1 
# 1 2 3 4 5 6 7 8


def solution(data):
    result = []
    for idx ,first in enumerate(data,0):
        print(idx)
        if idx == len(data)-1:
            break
        elif first < data[idx+1]:
            result.append("asc")
        elif first > data[idx+1]:
            result.append("desc")
    if "asc" in result and "desc" in result :
        return "mixed"
    elif "asc" in result and "desc" not in result :
        return "ascending"
    else:
        return "descending"

print(solution([1, 2, 3, 4, 5, 6, 7, 8]))
print(solution([8, 7, 6, 5, 4, 3, 2, 1]))
print(solution([8, 1, 7, 2, 6, 3, 5, 4]))

# 만약에 리스트로 값이 안들어 오고 입력값으로 들어 온다면?

def solution2():
    a = list(map(int, input().split(' ')))
    asc = True
    desc = True

    for i in range(1,8):
        if a[i] > a[i-1]:
            desc = False
        elif a[i] < a[i-1]:
            asc = False
    if asc:
        return "ascending"
    elif desc:
        return "descending"
    return "mixed"

# list index out of range 에러 떄문에 
# 리스트 인덱싱 사용 시 기본것 보다 -1로 비교하는게 훨신 편하게 할듯