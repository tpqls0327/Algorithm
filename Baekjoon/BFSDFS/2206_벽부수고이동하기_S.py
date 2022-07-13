# 벽 부수고 이동하기 

import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 방문 체크를 2가지 케이스로 나눠서 진행해야함
# [0, 0] : 지나지않은케이스, 벽을 지나온케이스
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]


def bfs():
    # 큐: x, y, 벽을 뚫었는지 여부 (1이면 이제 벽 못뚫음.)
    queue = deque([(0, 0, 0)])
    visited[0][0][0] = 1  # 비용 
    

    while queue:
        x, y, flag = queue.pop()

        # 무작정 방문했다고 컨티뉴 날려버리면안됨. 두가지 경우로 나눠야함.
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
