# 정확한 순위 2022-06-29

import sys
input = sys.stdin.readline

INF = int(1e9)
n,m = map(int, input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기자신 비용 0으로 초기화
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

# 간선정보 입력
for i in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1

# 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과 출력
result = 0
for a in range(1, n+1):
    cnt = 0
    for b in range(1, n+1):
        if graph[a][b] != INF or graph[b][a] != INF:
            cnt += 1
    if cnt == n:
        result += 1
print(result)

    
