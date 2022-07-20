import sys

# input = sys.stdin.readline
n = int(input())
origin = list(map(int, input().split()))
stack, ans = [0], [-1] * n

for i in range(1, n):
    while stack and origin[stack[-1]] < origin[i]:
        ans[stack.pop()] = origin[i]
    stack.append(i)
print(ans)
