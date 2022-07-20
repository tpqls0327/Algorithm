# 종이의 개수

import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = [0] * 3

def check(x, y, n):
    temp = arr[x][y]
    for i in range(n):
        for j in range(n):
            if temp != arr[x + i][y + j]:
                return False
    return True

def divide(x, y, n):
    if check(x, y, n):
        result[arr[x][y] + 1] += 1
    else:
        for i in range(3):
            for j in range(3):
                divide(x + i* n//3, y + j* n//3, n//3)              
    return

divide(0, 0, n)
for i in range(3):
    print(result[i])

