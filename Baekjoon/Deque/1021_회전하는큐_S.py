# 1021 회전하는 큐

from collections import deque

n,m = map(int, input().split())
data = list(map(int, input().split()))
q = deque()
for i in range(1, n+1):
    q.append(i)

ans = 0
idx = 0
while idx <m:
    if q[0] == data[idx]:
        q.popleft()
        idx += 1
    else:
        cnt = q.index(data[idx])
        if cnt <= len(q) / 2:
            q.rotate(-1)
            ans += 1
        else:
            q.rotate(1)
            ans += 1
print(ans)
        
