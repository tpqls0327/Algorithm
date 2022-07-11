# 나이트의 이동

from collections import deque
import sys
input = sys.stdin.readline

dx = [-2,-1,-2,-1,1,2,1,2]   # 왼쪽위, 왼쪽아래, 오른쪽위, 오른쪽아래
dy = [-1,-2,1,2,-2,-1,2,1]

def bfs(arr, x1, y1, x2, y2, l):
    q = deque()
    q.append((x1,y1))
    arr[x1][y1] = 1

    while q:
        x,y = q.popleft()
        if x == x2 and y == y2:
            return arr[x2][y2]-1
        
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= l or ny >= l:
                continue
            if arr[nx][ny] == 0:
                q.append((nx,ny))
                arr[nx][ny] = arr[x][y] + 1
    

for _ in range(int(input())):
    l = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    arr = [[0]*l for _ in range(l)]
    if x1 == x2 and y1 == y2:
        print(0)
        continue
    result = bfs(arr, x1, y1, x2, y2, l)
    print(result)
    
