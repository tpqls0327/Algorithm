ans = 0
for _ in range(int(input())):
    stack = []
    for s in input():
        stack.pop() if stack and stack[-1] == s else stack.append(s)
    ans += 0 if stack else 1
print(ans)
