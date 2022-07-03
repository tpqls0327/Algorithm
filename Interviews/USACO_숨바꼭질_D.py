import heapq
INF = int(1e9)
n, m = map(int, input().split())
form = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    s, e = map(int, input().split())
    form[e].append([s, 1])
    form[s].append([e, 1])


def dij():
    q = []
    heapq.heappush(q, [0, 1])
    distance[1] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in form[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])


dij()
max_n = 0
max_d = 0
res = []
for i in range(1, n+1):
    if max_d < distance[i]:
        max_n = i
        max_d = distance[i]
        res = [max_n]
    elif max_d == distance[i]:
        res.append(i)

print(max_n, max_d, len(res))

"""
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2

"""