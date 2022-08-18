import sys
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(int(input()))]
for i, j in sorted(arr, key=lambda x: (x[0], x[1])):
    print(i, j)
