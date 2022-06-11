# 인구이동
from collections import deque
import math

N, L, R = map(int, input().split())
arr = []
for i in range(N):
    a = list(map(int, input().split()))
    arr.append(a)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

result = 0 # 인구이동
while True:
    union = []    # 연합국가
    visited = [[False] * N for _ in range(N)]

    # bfs
    for i in range(N):
        for j in range(N):
            q = deque()
            q.append((i,j))
            nation = [[i,j]]
            visited[i][j] = True
            
            while q:
                x,y = q.popleft()
                if visited[x][y] == True:
                    continue
                
                for idx in range(4):
                    nx = x + dx[idx]
                    ny = y + dy[idx]
                    
                    if nx < 0 or ny < 0 or nx >= N or ny >= N:
                        continue
                    
                    data = abs(arr[x][y]-arr[nx][ny]) 
                    if data >= L and data <= R:
                        visited[nx][ny] = True
                        nation.append([nx,ny])
                        q.append((nx,ny))
                        
            union.append(nation)
            
    if union == []:
        break
    else:
        print(union)
        result += 1

        # 연합국 값 나누기
        for u in union:
            num = math.trunc(sum(u) / len(u))
            for i in u:
                arr[i[0]][i[1]] = num
            
    
