import sys

# input = sys.stdin.readline
n = int(input())
origin = [int(input()) for _ in range(n)]
stack, ans = [], 0

for i in range(n):
    print(stack)
    cnt = 1
    while stack and stack[-1][0] <= origin[i]:
        ans += stack[-1][1]
        cnt += stack[-1][1] if stack[-1][0] == origin[i] else 0
        stack.pop()
    ans += 1 if stack else 0
    stack.append([origin[i], cnt])
print(ans)
