from collections import deque
import sys

# input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m = map(int, input().split())
board = []
ice = deque()
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        if tmp[j]:
            ice.append([i, j])
    board.append(tmp)

days = 0
while ice:
    days += 1
    ice_tmp = deque()

    # 녹아야 할 빙산량 계산
    while ice:
        x, y = ice.popleft()
        ice_cnt = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not board[nx][ny]:
                ice_cnt += 1
        ice_tmp.append([x, y, ice_cnt])

    # 빙산 녹이기
    while ice_tmp:
        i, j, c = ice_tmp.popleft()
        if board[i][j] - c > 0:
            board[i][j] -= c
            ice.append([i, j])
        else:
            board[i][j] = 0

    # 쪼개진 빙산 검사
    block = 0
    visited = [[0] * m for _ in range(n)]
    for i, j in ice:
        if not visited[i][j] and board[i][j]:
            block += 1
            visited[i][j] = 1
            q = deque([[i, j]])

            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]

                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny]:
                        q.append([nx, ny])
                        visited[nx][ny] = 1

    if block >= 2:
        break

print(days if ice else 0)
