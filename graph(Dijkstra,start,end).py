# 다익스트라 알고리즘 시작과 끝 최단경로 출력
# 최단 경로 출력
# - 탐색할 그래프의 시작 정점과 다른 정점들간의 최단 거리 및 최단 경로 출력하기

# 다익스트라 시간복잡도 
# 1) 각 노드의 인접한 간선을 모두 검사
# 2) 우선순위 큐에 노드/거리 정보를 넣고(push) 삭제(pop)하는 과정

# 1)의 시간복잡도 : O(E) 각노드는 최대 한번씩 방문함으로 그래프의 모든간선은 최대 한번 씩 검사 
# 2)의 시간복잡도 : 우선순위 큐에 가장 많은노드 거리정보가 들어가는 경우 넣고 삭제하는 경우가 걸림
#                  모든 간선이 검사될 때 마다 배열의 최단거리 갱신
#                  간선추가시 O(E) 노드 거리정보를 O(logE)걸림 = O(ElogE)
# 결과 :O(ElogE)

# 힙의 시간복잡도
# 그래프의 높이를 h라고 하면 n개의 노드를 데이터 삽입삭제시, 최악의 경우 root에서 leaf까지 비교해야되서
# h = O(logn)의 시간 복잡도를 가진다.

import heapq

def dijkstra_start_end(graph, start, end):

    # 시작 정점에서 각 정점까지의 거리를 저장할 딕셔너리 생성, 무한대(inf)로 초기화
    distance_array = {vertex: [float('inf'), start] for vertex in graph}
    distance_array[start] = [0,start]
    priority_queue = []

    # 그래프의 시작 정점과 시작 정점의 거리(0)을 최소힙에 넣어줌
    heapq.heappush(priority_queue, [distance_array[start][0], start])

    # 큐에서 정점을 하나씩 꺼내 인접한 정점들의 가중치를 모두 확인하여 업데이트
    while priority_queue:

        # 큐에서 정점을 하나씩 꺼내 인접한 현재 정점과 현재 가중치를 pop 
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # 더 짧은 거리가 있다면 무시한다.
        if distance_array[current_vertex][0] < current_distance:
            continue
        
        # 현재 정점을 주어진 그래프에서의 정점과 가중치를 가지고
        for adjacent, weight in graph[current_vertex].items():

            # distance : 시작 정점에서 인접 정점의 합
            distance = current_distance + weight
            # 만약 시작 정점에서 인접 정점으로 바로 가는 것보다 현재 정점을 통해 가는 것이 더 가까울 경우
            if distance < distance_array[adjacent][0]:
                # 거리를 업데이트
                distance_array[adjacent] = [distance, current_vertex]
                heapq.heappush(priority_queue, [distance, adjacent])

    # end값을 path라고 하고 넣어줌
    path = end
    path_output = end + '->'

    # 마지막 노드의 값이 start값과 일치할때 까지
    while distance_array[path][1] != start:
        # 하나씩 추가
        path_output += distance_array[path][1] + '->'
        # 마지막 노드의 값과 가장 가까운 노드로 대체
        path = distance_array[path][1]
    path_output += start
    print(path_output)
    #F->E->D->A
    return distance_array


graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}
print(dijkstra_start_end(graph, 'A', 'F'))
#{'A': [0, 'A'], 'B': [6, 'C'], 'C': [1, 'A'], 'D': [2, 'A'], 'E': [5, 'D'], 'F': [6, 'E']}