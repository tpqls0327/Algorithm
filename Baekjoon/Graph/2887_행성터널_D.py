def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
parent = [i for i in range(n+1)]
plant = [list(map(int, input().split()))+[i] for i in range(n)]
edges = []

for i in range(3):
    tmp = sorted(plant, key=lambda x: x[i])
    for k in range(n-1):
        c = [abs(tmp[k+1][i] - tmp[k][i]), tmp[k][3], tmp[k+1][3]]
        edges.append(c)

edges.sort()
total_cost = 0

for edge in edges:
    c, a, b = edge

    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        total_cost += c
print(total_cost)
