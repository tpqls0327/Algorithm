# 경쟁적 전염
from collections import deque

# 입력란
n, k = map(int, input().split())
maps = []
virus = []
for i in range(n):
    maps.append(list(map(int, input().split())))
    for j in range(n):
        if maps[i][j] != 0:
            virus.append([maps[i][j],i,j])
s,x,y = map(int, input().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# bfs
def bfs(s,x,y):
    q = deque(virus)
    count = 0
    
    while q:
        if count == s:
            break
        for _ in range(len(q)):
            v = q.popleft()
            for i in range(4):
                bx = v[1]+dx[i]
                by = v[2]+dy[i]         
                if 0 <= bx < n and 0 <= by < n:
                    if maps[bx][by] == 0 :
                        maps[bx][by] = v[0]
                        q.append([v[0],bx,by])       
        count+=1
    return (maps[x-1][y-1])
virus.sort()
print(bfs(s,x,y))

