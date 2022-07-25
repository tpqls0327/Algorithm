# N과 M(2)

from itertools import combinations

n,m = map(int, input().split())
arr = []
for i in range(1,n+1):
    arr.append(i)
for data in combinations(arr,m):
    print(*data)
