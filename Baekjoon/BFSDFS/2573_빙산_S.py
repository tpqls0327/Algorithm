# 빙산

from collections import deque
import sys
input = sys.stdin.readline

# 입력
n,m = map(int, input().split())
arr = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

# 빙산의 위치 찾기 
iceberg = []
for i in range(n):
    for j in range(m):
        if arr[i][j] != 0:
            iceberg.append([i,j])

dx = [-1,1,0,0]
dy = [0,0,-1,1]

q = deque(iceberg)
melt_q = deque()

result = 0
result_cnt = 0
while True:
    # step1) 빙산이 두 덩어리로 분리되었는지 확인
    count = 0
    visited = [[False]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0 and visited[i][j] == False:
                melt_q.append([i,j])
                while melt_q:
                    data = melt_q.popleft()

                    x = data[0]
                    y = data[1]
                    visited[x][y] = True
                    count += 1
                    
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < m:
                            if arr[nx][ny] != 0 and visited[nx][ny] == False:
                                visited[nx][ny] = True
                                melt_q.append([nx,ny])
                  
                if len(q) != count:
                    result_cnt = 1
                    break
        if result_cnt == 1:
            break
    if result_cnt == 1:
        print(result)
        break

    # step2) 전부 녹았는데 두 덩어리로 분리되지 않았을 경우
    melted = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                melted += 1
    if melted == n*m:
        print(0)
        break

    # step3) 빙산 녹이기
    melted_iceberg = []    # 녹은 빙산 
    for t in range(len(q)):
        data = q.popleft()
        x = data[0]
        y = data[1]
        
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if arr[nx][ny] == 0:
                cnt += 1
                
        arr[x][y] -= cnt
        if arr[x][y] <= 0:
            arr[x][y] = -1
            melted_iceberg.append([x,y])
        else:
            q.append([x,y])
        
    # step4) 녹은 빙산을 0으로 바꾸어 주기
    for melted in melted_iceberg:
        mx,my = melted
        arr[mx][my] = 0
    result += 1

    
