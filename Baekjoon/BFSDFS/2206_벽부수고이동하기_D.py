from collections import deque
import sys

input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1


def bfs():
    deq = deque()
    deq.append([0, 0, 0])

    while deq:
        x, y, c = deq.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][c]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == '1' and c == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    deq.append([nx, ny, 1])
                elif board[nx][ny] == '0' and visited[nx][ny][c] == 0:
                    visited[nx][ny][c] = visited[x][y][c] + 1
                    deq.append([nx, ny, c])
    return -1


print(bfs())
