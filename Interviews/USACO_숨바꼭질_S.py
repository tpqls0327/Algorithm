# 숨바꼭질
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())

graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
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
dijkstra(1)

result = []
cnt = distance.index(max(distance[1:]))
result.append(cnt)    # 숨어야하는 헛간 번호
result.append(distance[cnt])     # 헛간 까지의 거리 
result.append(distance.count(distance[cnt]))     # 헛간과 같은 거리를 갖는 헛간의 개수
result = ' '.join(map(str, result))
print(result)

    
