# 특정 거리의 도시 찾기
from collections import deque

def bfs(graph, start, visited):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        node = queue.popleft()
        for now, dist in graph[node]:
            if not visited[now]:
                distance[now] = distance[node]+dist
                queue.append(now)
                visited[now] = True   
    return graph

# 그래프의 기본정보 저장 
n,m,k,x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    # 노드, 간선
    graph[a].append((b,1))
    
visited = [False] * (n+1)
distance = [0] * (n+1)

bfs(graph, x, visited)

# 최단거리가 k인 도시의 번호 출력 
answer = []
for idx, dist in enumerate(distance):
    if dist == k:
        answer.append(idx)
if not answer:
    print(-1)
else:
    answer.sort()
    for ans in answer:
        print(ans)
