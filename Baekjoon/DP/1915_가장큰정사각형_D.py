n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        if i > 0 and j > 0 and board[i][j] == 1:
            board[i][j] += min(board[i-1][j-1], board[i-1][j], board[i][j-1])
        ans = max(board[i][j], ans)

print(ans**2)
