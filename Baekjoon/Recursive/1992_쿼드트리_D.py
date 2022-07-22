import sys
sys.setrecursionlimit(10000)
# input = sys.stdin.readline
n = int(input())
board = [list(map(int, list(input()))) for _ in range(n)]
ans = []


def ze(x, y, size):
    global ans
    if size < 1:
        ans.append('(')
        for i in range(x, x + size):
            for j in range(y, y + size):
                ans.append(str(board[i][j]))
        ans.append(')')
        return
    start = board[x][y]

    for i in range(x, x+size):
        for j in range(y, y+size):
            if board[i][j] != start:
                ans.append('(')
                tmp = size // 2
                for a in range(x, x + size, tmp):
                    for b in range(y, y + size, tmp):
                        ze(a, b, tmp)
                ans.append(')')
                return

    ans.append(str(start))


ze(0, 0, n)

print(''.join(ans))
