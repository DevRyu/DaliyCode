# 최단경로 문제(방향, 가중치 그래프)
# 두노드를 잇는 가장 짧은 경로를 찾는 문제
# 가중치 그래프에 노드(edge)의 가중치의 합이 최소가 되도록 하는 경로를 찾는 것이 목적

# 1. 단일 출발 단일 도착(single-source and single-destination shortest path problem)
# 그래프 내에 특정노드 u에서 출발 특정노드 v에 도착하는 것

# 2. 단일 출발 최단 경로 문제(single-source shortest path problem)
# 그래프 내의 특정 노드 u와 그래프 내 다른 모든 노드 각각의 가장 짧은 경로를 찾는 문제
# 특정 노드가 A면 A 외 모든 노드인 B, C, D 각 노드와 A 간에 (즉, A - B, A - C, A - D) 각각 가장 짧은 경로를 찾는 문제를 의미함
# 3. 전체 쌍 최단 경로 : 그래프 내의 모든 노드 쌍 (u,v)에 대한 최단 경로를 찾는 문제

# 최단 경로 알고리즘 - 다익스트라 알고리즘(단일 출발 최단 경로 문제)
# 다익스트라 알고리즘은 위 최단 경로 문제 종류중 2번에 해당
# ->하나의 정점에서 다른 모든 정점 간의 가장 짧은 거리를 구하는 문제

# 다익스트라 알고리즘 로직 특징
# 첫 정점을 기준으로 연결되어 있는 정점들을 추가하며 최단 거리를 갱신하는 방법
# BFS알고리즘과 유사(첫 노드부터 각노드간의 거리를 저장하는 배열(큐) 만든 후 인접노드 간의 거리계산, 노드간 짧은 거리를 구함)
# -> 우선순위 큐를 사용하는 방식

# 우선순위 큐를  활용한 다익스트라 알고리즘
# -> MinHeap 방식을 활요해서 현재 가장 짧은 거리를 가진 노드 정보를 먼저 꺼내게 됨

# 1) 초기화 
# ->첫정점을 기준으로 배열 선언(거리 저장 배열), 정점에서 각 정점까지의 거리를 저장
# -> 첫 정점의 거리는 0, 나머지는 무한대(infinite)로 저장
# -> 우선순위 큐에 (첫 정점, 거리 0)만 먼저 넣음

# 2) 우선순위 큐(최소 힙)에서 노드를 꺼냄
# -> 우선순위 큐에서 추출한 (A, 0) [노드, 첫 노드와의 거리] 를 기반으로 인접한 노드와의 거리 계산
# -> 처음에 첫 정점만 저장되어 꺼내짐
# -> 첫 정점에 인접한 노드들 각각에 가는 거리와 현재 배열에 저장되어 있는 첫 정점에서 각정점까지의 거리를 비교
# -> 배열에 저장된 거리보다, 첫 정점에서 해당노드로 가는 길이가 짧을 경우, 배열에 해당 노드의 거리 업데이트
# -> 배열에 해당 노드의 거리가 업데이트 될 시, 우선순위 큐에 넣음
# --> 결과적으로  너비 우선 탐색 방식과 유사하게 첫 정점에 인접한 노드 순차 방문
# --> 만약 배열에 기록된 현재까지 발견된 가장 짧은 거리보다, 더 긴 거리(루트)를 가진 (노드,거리)의 경우 계산 안함
# ---> 만약 방향성에서 갈 길이 없거나 이미 최단 거리가 있다면 생략한다.
# 3) 1),2) 반복하면 우선순위 큐에 꺼낼 노드가 없을 때까지

# 우선순위 큐 사용시 장점
# 지금까지 발견된 가장 짧은 거리의 노드에 대해 먼저 계산
# 더 긴 거리로  계산된 루트에 대해서는 계산을 스킵

# 힙 큐(우선순위 큐) 예시

import heapq

queue = []

heapq.heappush(queue, [2, 'A'])
heapq.heappush(queue, [5, 'B'])
heapq.heappush(queue, [1, 'C'])
heapq.heappush(queue, [7, 'D'])
print (queue)
# [[1, 'C'], [5, 'B'], [2, 'A'], [7, 'D']]
for index in range(len(queue)):
    # heappop 큐를 처음인덱스 부터 pop한다.
    print (heapq.heappop(queue))
    # [1, 'C']
    # [2, 'A']
    # [5, 'B']
    # [7, 'D']

# 그래프 예시
mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

def dijkstra(graph, start):
    # 그래프 거리 저장 배열을 infintie값인 딕셔너리로 초기화 세팅
    distances = {node : float('inf') for node in graph}
    distances[start] = 0
    # 리스트를 만들고
    queue = []
    # 위 리스트를 힙 큐로 재생산 // 힙 큐에 빈값과 시작값 0 과 시작 키 넣어준다.
    heapq.heappush(queue, [distances[start], start])
    print('init heapq', queue) # init heapq [[0, 'A']]
    # 힙큐에 값이 있을 떄
    while queue:
        # 첫번째 힙큐 인덱스값을 pop해서 현재 거리 값와 현재 노드에 저장한다.
        print("heap queue의 상태",queue)
        cur_distance, cur_node = heapq.heappop(queue)
        print("heap queue의 cur_distance, cur_node",cur_distance, cur_node)
        # 현재 노드키의 그래프 거리 배열의 값보다 현재 거리가 크면 생략
        # 어짜피 계산 할 필요가 없으니까
        if distances[cur_node] < cur_distance:
            continue
        # 큐에서의
        # 키에 해당하는 인접 노드의 키 adjacent
        # 그 키에 인접한 노드들의 값 weight 
        for adjacent, weight in graph[cur_node].items():
            # 힙큐에서의 노드의 거리 값(cur_distance)와 
            # 인접한 노드의 값을 더한다. 
            distance = cur_distance + weight
            print("adjacent,weight", adjacent,weight)
            # 합의 결과가 기존의 인접노드의 그래프 거리보다 작다면 
            # 최소 값보다 작다면
            if distance < distances[adjacent]:
                # 값을 바꾸고
                distances[adjacent] = distance
                # 힙큐에 값을 추가해 준다.
                heapq.heappush(queue, [distance,adjacent])
                print("distance < distances[adjacent]임으로 heap queue 추가",queue)
                print("distances 그래프 거리 배열",distances)
    return distances

print("result:",dijkstra(mygraph, 'A'))
# result: {'A': 0, 'B': 6, 'C': 1, 'D': 2, 'E': 5, 'F': 6}

# heap queue의 상태 [[0, 'A']]
# heap queue의 cur_distance, cur_node 0 A
# adjacent,weight B 8
# distance < distances[adjacent]임으로 heap queue 추가 [[8, 'B']]
# distances 그래프 거리 배열 {'A': 0, 'B': 8, 'C': inf, 'D': inf, 'E': inf, 'F': inf}
# adjacent,weight C 1
# distance < distances[adjacent]임으로 heap queue 추가 [[1, 'C'], [8, 'B']]
# distances 그래프 거리 배열 {'A': 0, 'B': 8, 'C': 1, 'D': inf, 'E': inf, 'F': inf}
# adjacent,weight D 2
# distance < distances[adjacent]임으로 heap queue 추가 [[1, 'C'], [8, 'B'], [2, 'D']]
# distances 그래프 거리 배열 {'A': 0, 'B': 8, 'C': 1, 'D': 2, 'E': inf, 'F': inf}

# heap queue의 상태 [[1, 'C'], [8, 'B'], [2, 'D']]
# heap queue의 cur_distance, cur_node 1 C
# adjacent,weight B 5
# distance < distances[adjacent]임으로 heap queue 추가 [[2, 'D'], [8, 'B'], [6, 'B']]
# distances 그래프 거리 배열 {'A': 0, 'B': 6, 'C': 1, 'D': 2, 'E': inf, 'F': inf}
# adjacent,weight D 2

# heap queue의 상태 [[2, 'D'], [8, 'B'], [6, 'B']]
# heap queue의 cur_distance, cur_node 2 D
# adjacent,weight E 3
# distance < distances[adjacent]임으로 heap queue 추가 [[5, 'E'], [8, 'B'], [6, 'B']]
# distances 그래프 거리 배열 {'A': 0, 'B': 6, 'C': 1, 'D': 2, 'E': 5, 'F': inf}
# adjacent,weight F 5
# distance < distances[adjacent]임으로 heap queue 추가 [[5, 'E'], [7, 'F'], [6, 'B'], [8, 'B']]
# distances 그래프 거리 배열 {'A': 0, 'B': 6, 'C': 1, 'D': 2, 'E': 5, 'F': 7}

# heap queue의 상태 [[5, 'E'], [7, 'F'], [6, 'B'], [8, 'B']]
# heap queue의 cur_distance, cur_node 5 E
# adjacent,weight F 1
# distance < distances[adjacent]임으로 heap queue 추가 [[6, 'B'], [6, 'F'], [8, 'B'], [7, 'F']]
# distances 그래프 거리 배열 {'A': 0, 'B': 6, 'C': 1, 'D': 2, 'E': 5, 'F': 6}

# heap queue의 상태 [[6, 'B'], [6, 'F'], [8, 'B'], [7, 'F']]
# heap queue의 cur_distance, cur_node 6 B

# heap queue의 상태 [[6, 'F'], [7, 'F'], [8, 'B']]
# heap queue의 cur_distance, cur_node 6 F
# adjacent,weight A 5

# heap queue의 상태 [[7, 'F'], [8, 'B']]
# heap queue의 cur_distance, cur_node 7 F

# heap queue의 상태 [[8, 'B']]
# heap queue의 cur_distance, cur_node 8 B
