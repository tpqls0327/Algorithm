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


g = int(input())
p = int(input())

parent = [i for i in range(g+1)]

ans = 0
for _ in range(p):
    tmp = find_parent(parent, int(input()))
    if tmp == 0:
        break
    union_parent(parent, tmp, tmp-1)
    ans += 1

print(ans)

"""
4
3
4
1
1

"""
"""
4
6
2
2
3
3
4
4

"""