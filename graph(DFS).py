# 23-18 깊이우선 탐색
 
# BFS(Breadth First Search) : 노드들과 같은 레벨에 있은 노드들 큐방식으로
# DFS(Depth First Search) : 노드들의 자식들을 먼저 탐색하는 스택방식으로 

# 스택 방식으로 visited, need_visited 방식으로 사용한다.

# 방법 : visited 노드를 체우는 작업
# 1) 처음에 visited에 비어있으니 시작 노드의 키를 넣고
# 2) 시작 노드의 값에 하나의 값(처음또는마지막 인접노드들)을 need_visit에 넣는다,
# 2-1) 인접노드가 2개 이상이면 둘 중 원하는 방향애 따라서 순서대로 데이터를 넣으면 된다. 
# 3) need_visit의 추가한 노드 키를 visited에 넣고 해당 값들을 need_visited에 넣는다. 
# 4) visited에 있으면 패스한다.
# 5) need_visited는 스택임으로 마지막의 값을 pop해서 key값은 visited need_visited에 value를 넣음
# 6) 반복

# 예시)
graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

def dfs(graph,start):
    visited = list()
    need_visit = list()
    # 시작값
    need_visit.append(start)

    count = 0
    # need_visit == 0 이될때까지
    while need_visit:
        count += 1
        # need_visit에 마지막 값을 pop(삭제)후 node에 넣어주고 (temp역할)
        node = need_visit.pop()
        # 방문한 값에 ㅇ벗다면
        if node not in visited:
            #방문 값에 넣어주고
            visited.append(node)
            # node의 값을 need_visit 에 추가
            need_visit.extend(graph[node])

    return visited 

dfs(graph,'A')

# 시간 복잡도 
# BFS 시간복잡도
# Vertex(노드) 수 : V
# Edge(간선) 수 : E
# 시간 복잡도 O(v+E)