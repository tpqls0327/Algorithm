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


n, m = map(int, input().split())
parent = [i for i in range(n+1)]

edges = []
cost = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append([c, a, b])

edges.sort()
total_cost = 0
for edge in edges:
    c, a, b = edge
    total_cost += c
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        cost += c
print(total_cost - cost)

"""
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11

"""
