import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
max_ = [0 for _ in range(n+1)]

for i in range(n-1, -1, -1):
    if arr[i][0] + i > n:
        max_[i] = max_[i+1]
    else:
        max_[i] = max(max_[i+1], arr[i][1] + max_[i + arr[i][0]])

print(max_[0])
