# 23-18 너비우선 탐색
# 그래프의 탐색 알고리즘
# BFS(Breadth First Search) : 노드들과 같은 레벨에 있은 노드들(같은 레벨 끼리)을 먼저 탐색하는 방식
# DFS(Depth First Search) : 노드들의 자식들을 먼저 탐색하는 방식

# 그래프를 코드로 표현하는 방법
# -> 시작 노드부터 끝노드 까지 딕셔너리 키로 만들고 해당 노드와 인접되어 있는 값들을 벨류로 만든다.

# 24-18 너비우선 탐색2
# 자료구조 큐를 두 개 활용함
# 방문한 노드들을 큐자료형에 (visited)
# 방문해야할 노드들을 큐 자료형에 (need_visit)

# 방법 : visited 노드를 체우는 작업
# 1) 처음에 visited에 비어있으니 시작 노드의 키를 넣고
# 2) 시작 노드의 값들을 need_visit에 넣는다,
# 3) need_visit의 값을 순차적으로 뽑아서 visited에 키로 넣는다. visited에 있으면 패스
# 4) 두번째로 넣은 visited키의 값들을 다시 need_visit에 넿는다
# 5) 만약 visited에 키가 있으면 생략
# 6) 반복


# 25-18 너비우선 탐색3
# 간단하게 큐를 안쓰고 리스트의 자료형을 이용한다.

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

def bfs(graph, start):
    visited = list()
    need_visit = list()

    #시작 노드를 need_visited에 먼저 넣고
    need_visit.append(start)
    count = 0
    # need_visit 방문해야할 큐가 다 비어져 있다면
    while need_visit:
        count += 1
        # 큐의 방식대로 첫번째 인덱스를 pop(삭제)함
        node = need_visit.pop(0)
        # 노드가 visited에 없으면 
        # 1)visited에 노드 키를 넣는다.
        # need_visit에 그래프 노드의 값들을 넣는다.
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    # 시간 복잡도
    print(count) # 19
    # 방문 한 노드들의 순서를 visited에 넣어 리턴
    return visited
bfs(graph, 'A')
# BFS 시간복잡도
# Vertex(노드) 수 : V
# Edge(간선) 수 : E
# 시간 복잡도 O(v+E)