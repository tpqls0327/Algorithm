import sys

# input = sys.stdin.readline
n = int(input())
origin = [int(input()) for _ in range(n)]
stack, cnt = [], 0

for i in range(n):
    while stack and stack[-1] <= origin[i]:
        stack.pop()
    stack.append(origin[i])
    cnt += len(stack)-1

print(cnt)
