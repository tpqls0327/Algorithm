import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

ans = 0
for a in range(1, n+1):
    cnt = 0
    for b in range(1, n+1):
        if graph[a][b] != INF or graph[b][a] != INF:
            cnt += 1
    if cnt == n:
        ans += 1
print(ans)

"""
6 6
1 5
3 4
4 2
4 6
5 2
5 4

"""