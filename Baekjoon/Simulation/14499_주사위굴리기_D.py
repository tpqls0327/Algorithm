n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
command = list(map(int, input().split()))
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
dice = [0] * 6


def turn(pos):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if pos == 1:    # 동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    elif pos == 2:  # 서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    elif pos == 3:  # 북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
    else:           # 남
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e


nx, ny = x, y
for i in command:
    nx += dx[i - 1]
    ny += dy[i - 1]

    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        nx -= dx[i - 1]
        ny -= dy[i - 1]
        continue

    turn(i)
    if board[nx][ny] == 0:
        board[nx][ny] = dice[-1]
    else:
        dice[-1] = board[nx][ny]
        board[nx][ny] = 0

    print(dice[0])
