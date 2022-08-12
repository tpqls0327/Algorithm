from collections import deque

n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]


def direction(pos):
    dx, dy = [], []
    if pos == 0:
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]
    elif pos == 1:
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
    elif pos == 2:
        dx = [0, -1, 0, 1]
        dy = [1, 0, -1, 0]
    elif pos == 3:
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

    return dx, dy


q = deque()
q.append([r, c, d])
visited[r][c] = 1
is_continue = True
while q:
    # for v in visited:
    #     print(v)
    # print()
    x, y, z = q.popleft()
    tx, ty = direction(z)
    for i in range(4):
        nx = x + tx[i]
        ny = y + ty[i]

        if 0 > nx or nx >= n or 0 > ny or ny >= m:
            if i == 0:
                z = z - 1 if z > 1 else 3
                q.append([x, y, z])
            break

        if board[nx][ny] == 0 and not visited[nx][ny]:
            visited[nx][ny] = 1
            for _ in range(i+1):
                if z - 1 < 0:
                    z = 3
                else:
                    z -= 1
            q.append([nx, ny, z])
            break
        elif i == 3:
            if board[x+tx[1]][y+ty[1]] == 0:
                q.append([x+tx[1], y+ty[1], z])


ans = 0
for v in visited:
    ans += sum(v)

print(ans)
