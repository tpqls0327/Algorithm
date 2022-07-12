from collections import deque
import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    global san_spot, fire_spot, board, visited
    while san_spot:
        temp = deque()
        while san_spot:
            x, y = san_spot.popleft()
            if (x == h-1 or y == w-1 or x == 0 or y == 0) and board[x][y] != "*":
                return board[x][y]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w and board[nx][ny] == '.' and board[x][y] != '*':
                    board[nx][ny] = board[x][y] + 1
                    temp.append([nx, ny])
        san_spot = temp

        temp = deque()
        while fire_spot:
            x, y = fire_spot.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and board[nx][ny] != '#':
                    board[nx][ny] = '*'
                    visited[nx][ny] = 1
                    temp.append([nx, ny])
        fire_spot = temp


for _ in range(int(input())):
    w, h = map(int, input().split())
    board, fire_spot, san_spot = [], deque(), deque()
    visited = [[0] * w for _ in range(h)]
    for i in range(h):
        tmp = list(input())
        board.append(tmp)
        for j in range(w):
            if tmp[j] == '@':
                board[i][j] = 0
                san_spot.append([i, j])
            elif tmp[j] == '*':
                fire_spot.append([i, j])
                visited[i][j] = 1
    result = bfs()
    print(result+1 if result is not None else "IMPOSSIBLE")
