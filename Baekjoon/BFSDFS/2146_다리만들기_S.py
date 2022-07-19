import sys
from collections import deque
input = sys.stdin.readline

# 섬 분할 
def island(i, j):
    q = deque([(i, j)])
    arr[i][j] = gid
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == 1:
                    arr[nx][ny] = gid
                    q.append((nx, ny))
                elif arr[nx][ny] == 0 and not (x, y) in land:
                    land.append((x, y))

# 간척 사업 
def bridge(): 
    cnt = 0
    ans = int(1e9)
    while land:
        cnt += 1
        length = len(land)
        for _ in range(length):
            x, y = land.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if arr[nx][ny] == 0:
                        arr[nx][ny] = arr[x][y]
                        land.append((nx, ny))
                    elif arr[nx][ny] < arr[x][y]:
                        ans = min(ans, (cnt - 1) * 2)
                    elif arr[nx][ny] > arr[x][y]:
                        ans = min(ans, cnt * 2 - 1)
    return ans

dx, dy = (-1,1,0,0), (0,0,-1,1)
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
land = deque()
gid = -1

for i in range(n):
    for j in range(n):
        if arr[i][j] > 0:
            island(i, j)
            gid -= 1
print(bridge())

