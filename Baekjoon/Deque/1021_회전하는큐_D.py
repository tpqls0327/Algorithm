from collections import deque
n, m = map(int, input().split())
arr = list(map(int, input().split()))
q = deque([i for i in range(1, n+1)])
cnt = 0
for i in arr:
    while q[0] != i:
        if q.index(i) <= len(q)//2:
            q.rotate(-1)
            cnt += 1
        else:
            q.rotate(1)
            cnt += 1
    q.popleft()
print(cnt)
