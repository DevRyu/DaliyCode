# 백 트래킹 (backtracking)
# DFS방식을 사용, 
# 고려 할 수 있는 경우의 수를 상태공간트리(State Space Tree)를 사용
# - Promising: 해당 루트가 조건에 맞는지를 검사하는 기법
# - Pruning (가지치기): 조건에 맞지 않으면 포기하고 다른 루트로 바로 돌아서서, 탐색의 시간을 절약하는 기법


# N Queen 문제 
# NxN크기의 체스판에 N개의 퀸을 서로 공결할수 없게 하기
# promising : 수직체크 (현재 열 -위 아래 열) =0 , 대각선 체크(abs(퀸의 열 - 현재 열)= 1++) 

# is_available : promising 수직체크, 대각선 체크
def is_available(candidate, cur_col):
    # len(candidate) = 현재 행
    cur_row = len(candidate)
    # 현재 행 이전의 행들
    for queen_row in range(cur_row):
        # 수직 체크, 대각선 체크
        if candidate[queen_row] == cur_col or abs(candidate[queen_row]- cur_col) == cur_row- queen_row:
            return False
    return True

# dfs, 재귀로 해결
def dfs(N, cur_row, cur_candidate, result):
    #만약 현재 로우가 배치가 끝나면
    if cur_row == N:
        # 결과 값을 후보군에 추가
        result.append(cur_candidate[:])
        return

    # 한 행당 열들을 체크한다.
    for candidate_col in range(N):
        # pruning : 현재 후보군과  후보 열이 만족이되면
        if is_available(cur_candidate, candidate_col):
            # 후보군에 해당 열을 넣고
            cur_candidate.append(candidate_col)
            # 다음 행으로 +1 추가 하고 , 현재 후보군, 결과를 넣고
            dfs(N,cur_row +1 ,cur_candidate ,result)
            #백트래킹: 필요없는 현재 후보군은 pop
            cur_candidate.pop()


def n_queen(N):
    result = []
    dfs(N, 0, [], result)

    return result

print(n_queen(4))
# [[1, 3, 0, 2], [2, 0, 3, 1]]
# 1행 3행 0행 2행
# 2행 0행 3행 1행
# 위 두 가지 방법으로 해결하면 문제가 풀린다. 