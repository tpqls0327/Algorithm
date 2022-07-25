# 쿼드트리

import sys
input = sys.stdin.readline

def dfs(x, y, size):
    if size == 1:    
        print(arr[x][y], end="")
        return
    num = arr[x][y]

    for row in range(x, x + size):
        for col in range(y, y + size):
            if num != arr[row][col]:
                print("(", end="")
                size //= 2
                dfs(x, y, size)
                dfs(x, y + size, size)
                dfs(x + size, y, size)
                dfs(x + size, y + size, size)
                print(")", end="")
                return

    print(arr[x][y], end="")
    return


n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, list(input().rstrip()))))

dfs(0, 0, n)
