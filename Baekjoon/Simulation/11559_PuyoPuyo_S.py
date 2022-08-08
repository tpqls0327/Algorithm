# 11559 Puyo Puyo

from collections import deque
import sys
input = sys.stdin.readline

arr = [list(input()) for _ in range(12)]
dx,dy = [-1,1,0,0], [0,0,-1,1]

def bfs(x_,y_,visited, cnt):
    q = deque()
    q.append((x_,y_))
    result = []
    visited[x_][y_] = True

    while q:
        x,y = q.popleft()
        result.append([x,y])

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < 12 and ny >= 0 and ny < 6:
                if visited[nx][ny]:
                    continue
                if arr[nx][ny] == arr[x][y]:
                    visited[nx][ny] = True
                    q.append((nx,ny))
    if len(result) >= 4:
        cnt += 1
        for re in result:
            arr[re[0]][re[1]] = '.'
    return cnt

def check_fall():
    for i in range(10, -1, -1):
        for j in range(6):
            if arr[i][j] != '.' and arr[i+1][j] == '.':
                for k in range(i+1, 12):
                    if k == 11 and arr[k][j] == '.':
                        arr[k][j] = arr[i][j]
                    elif arr[k][j] != '.':
                        arr[k-1][j] = arr[i][j]
                        break
                arr[i][j] = '.'

ans = 0
while True:
    # 모든 data의 자리에서 상하좌우 비교
    # 하나가 터지면 자리를 내리고 계속 비교
    cnt = 0
    for i in range(12):
        for j in range(6):
            visited = [[False] * 6 for _ in range(12)]
            if arr[i][j] != '.':
                cnt = bfs(i,j,visited, cnt)
    if cnt == 0:
        print(ans)
        break
    else:
        ans += 1
    check_fall()
    
