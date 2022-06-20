import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            lu = 0
        else:
            lu = arr[i-1][j-1]

        if j == i:
            ru = 0
        else:
            ru = arr[i-1][j]

        arr[i][j] = arr[i][j] + max(lu, ru)

print(max(arr[n-1]))
