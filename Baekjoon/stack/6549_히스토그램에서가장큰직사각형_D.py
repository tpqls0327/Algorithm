import sys

# input = sys.stdin.readline
while True:
    area = list(map(int, input().split()))
    if not area[0]:
        break
    n, *origin = area
    stack, ans = [], 0
    for i in range(n):
        max_ = i
        while stack and stack[-1][0] >= origin[i]:
            h, v = stack.pop()
            ans = max(ans, (i-v)*h)
            max_ = v
        stack.append([origin[i], max_])

    while stack:
        h, v = stack.pop()
        ans = max(ans, (n-v)*h)
    print(ans)
