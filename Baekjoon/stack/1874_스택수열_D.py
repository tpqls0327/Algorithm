import sys

# input = sys.stdin.readline
n = int(input())
ori = [i for i in range(n, 0, -1)]
arr = [int(input()) for _ in range(n)]
ans = []
px = []
for i in range(n):
    while ori and arr[i] >= ori[-1]:
        ans.append(ori.pop())
        px.append('+')
    if arr[i] == ans[-1]:
        ans.pop()
        px.append('-')

print('NO' if ans else '\n'.join(px))
