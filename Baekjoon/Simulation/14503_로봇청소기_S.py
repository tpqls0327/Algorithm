# 14503 로봇 청소기
from collections import deque
import sys
input = sys.stdin.readline

def bfs(r,c,d):
    ans = 0
    visited = [[False]*m for _ in range(n)]
    q = deque()
    q.append((r,c))
        
    while q:
        x,y = q.popleft()
        if not visited[x][y]:
            ans+=1
        visited[x][y] = True   # 현재 위치 청소
        cnt = 0   # 네방향 이동 가능 여부
        for i in range(4):
            d = (d-1) % 4
            nx, ny = dx[d]+x, dy[d]+y
            if not visited[nx][ny] and arr[nx][ny] == 0:
                q.append((nx,ny))
                break
            else:
                cnt += 1
            # 네 방향 모두 청소되어 있는 경우
            if cnt == 4:
                # 뒤쪽 방향이 벽인 경우
                if arr[x+dx[(d-2)%4]][y+dy[(d-2)%4]] == 1:
                    return print(ans)
                q.append((x+dx[(d-2)%4],y+dy[(d-2)%4]))
    return print(ans)


n,m = map(int,input().split())
r,c,d = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
dx,dy = (-1,0,1,0), (0,1,0,-1)   # 북:0 동:1 남:2 서:3   cnt = (cnt-1) % 4

bfs(r,c,d)
