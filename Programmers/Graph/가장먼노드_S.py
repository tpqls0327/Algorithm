# 가장먼노드_S.py 20230313

import heapq
import sys

def solution(n, edges):
    
    INF = int(1e9)
    graph = [[] for i in range(n+1)]
    distance = [INF] * (n+1)
    
    # 모든 간선 정보를 입력받기
    for edge in edges:
        graph[edge[0]].append((edge[1],1))
        graph[edge[1]].append((edge[0],1))

    # 다익스트라    
    def dijkstra(start):
        q = []
        heapq.heappush(q, (0,start))
        distance[start] = 0

        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
    
    # 다익스트라 알고리즘을 수행
    dijkstra(1)
    
    # 모든 노드로 가기 위한 최단 거리를 출력
    max_num = [-1,0]
    for i in range(1, n+1):
        # 현재 최단거리보다 거리가 더 클때
        if max_num[0] < distance[i]:
            max_num[0] = distance[i]
            max_num[1] = 1
        # 현재 최단거리와 거리가 같을 때
        elif max_num[0] == distance[i]:
            max_num[1] += 1
            
    return max_num[1]
