from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    board = [[0]*n for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    dx, dy = [-2, -2, -1, 1, 2, 2, 1, -1], [-1, 1, 2, 2, 1, -1, -2, -2, -1]

    start_y, start_x = map(int, input().split())
    end_y, end_x = map(int, input().split())

    if start_y == end_y and start_x == end_x:
        print(0)
        continue

    board[start_y][start_x] = 1
    visited[start_y][start_x] = 1

    que = deque()
    que.append([start_y, start_x, 0])

    while que:
        x, y, c = que.popleft()

        if x == end_y and y == end_x:
            print(c)
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = 1
                que.append([nx, ny, c+1])

