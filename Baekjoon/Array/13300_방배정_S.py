# 방 배정

import math
import sys
input = sys.stdin.readline

n,k = map(int, input().split())
data = [[0,0] for _ in range(6)]
for i in range(n):
    a,b = map(int, input().split())
    data[b-1][a] += 1

result = 0
for i in range(6):
    for j in range(2):
        cnt = math.ceil(data[i][j] / k)
        result += cnt
print(result)
