# 탑승구

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

g = int(input())
p = int(input())
parent = [0] * (g + 1)

for i in range(1, g+1):
    parent[i] = i

result = 0
for i in range(p):
    n = int(input())
    data = find_parent(parent,n)
    if data == 0:
        break
    union_parent(parent,data-1,n)
    result += 1
print(result)
    
    
