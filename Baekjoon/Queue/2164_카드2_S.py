# 2164 카드2
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
data = [i for i in range(1,n+1,1)]
data = deque(data)

for _ in range(n-1):
    data.popleft()
    tmp = data.popleft()
    data.append(tmp)
print(data[0])
