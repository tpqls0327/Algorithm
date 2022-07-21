import sys
sys.setrecursionlimit(10000)
# input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans = [0]*2     # [0, 1]


def ze(x, y, size):
    if size < 1:
        return
    start = board[x][y]

    for i in range(x, x+size):
        for j in range(y, y+size):
            if board[i][j] != start:
                tmp = size // 2
                for a in range(x, x + size, tmp):
                    for b in range(y, y + size, tmp):
                        ze(a, b, tmp)
                return

    ans[start] += 1


ze(0, 0, n)

print('\n'.join(map(str, ans)))
