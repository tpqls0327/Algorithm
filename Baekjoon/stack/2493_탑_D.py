import sys

# input = sys.stdin.readline
n = int(input())
tops = list(map(int, input().split()))
stack, ans = [], [0] * n

for i in range(n):
    while stack and tops[stack[-1]] < tops[i]:
        stack.pop()
    if stack:
        ans[i] = stack[-1] + 1
    stack.append(i)

print(*ans)
