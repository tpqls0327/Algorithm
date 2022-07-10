from collections import deque

n, k = map(int, input().split())
arr = deque([i for i in range(1, n+1)])
yoo = []
i = 0
while arr:
    if i == k-1:
        yoo.append(arr.popleft())
        i = 0
    else:
        arr.append(arr.popleft())
        i += 1

print(f"<{', '.join(map(str, yoo))}>")
