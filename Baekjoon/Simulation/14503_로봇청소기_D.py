from collections import deque

n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]


def direction(pos):
    dx, dy = [], []
    if pos == 0:
        dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
    elif pos == 1:
        dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
    elif pos == 2:
        dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
    elif pos == 3:
        dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    return dx, dy


q = deque([[r, c, d]])
visited[r][c], ans = 1, 1
while q:
    x, y, z = q.popleft()
    tx, ty = direction(z)
    for i in range(4):
        nx, ny = x + tx[i], y + ty[i]

        if 0 > nx or nx >= n or 0 > ny or ny >= m:
            if not i:
                z = z - 1 if z >= 1 else 3
                q.append([x, y, z])
            break

        if not board[nx][ny] and not visited[nx][ny]:
            visited[nx][ny] = 1
            ans += 1
            for _ in range(i+1):
                z = z - 1 if z >= 1 else 3
            q.append([nx, ny, z])
            break
        elif i == 3 and not board[x+tx[1]][y+ty[1]]:
            q.append([x+tx[1], y+ty[1], z])

print(ans)
