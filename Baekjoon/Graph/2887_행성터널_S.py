# 행성터널

import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
parent = [i for i in range(n)]

edges = []
result = 0

for i in range(n):
    parent[i] = i

x = []
y = []
z = []
for i in range(n):
    a,b,c = list(map(int, input().split()))
    x.append([a, i])
    y.append([b, i])
    z.append([c, i])

x.sort()
y.sort()
z.sort()

for i in range(n-1):
    edges.append([abs(x[i][0]-x[i+1][0]), x[i][1], x[i+1][1]])
    edges.append([abs(y[i][0]-y[i+1][0]), y[i][1], y[i+1][1]])
    edges.append([abs(z[i][0]-z[i+1][0]), z[i][1], z[i+1][1]])

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)
