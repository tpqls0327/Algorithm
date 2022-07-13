# 벽 부수고 이동하기 

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# [0, 0] : 벽 부심x, 벽 부심o
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]

def bfs():
    # 큐: x, y, 벽을 뚫었는지 여부 (1이면 이제 벽 못뚫음.)
    queue = deque([(0, 0, 0)])
    visited[0][0][0] = 1  # 비용 
    
    while queue:
        x, y, flag = queue.pop()

        if x == n - 1 and y == m - 1:
            return visited[x][y][flag]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]         
            if 0 <= nx < n and 0 <= ny < m:                
                # 벽이 뚫여있고, 아직 방문하지 않은 상태
                if graph[nx][ny] == 0 and visited[nx][ny][flag] == 0:
                    queue.appendleft((nx, ny, flag))
                    visited[nx][ny][flag] = visited[x][y][flag] + 1
                # 벽이 막혀있는 상태
                elif graph[nx][ny] == 1 and flag == 0:
                    queue.append((nx, ny, 1))
                    visited[nx][ny][1] = visited[x][y][flag] + 1   # flag 0->1 변경 
    return -1

print(bfs())
