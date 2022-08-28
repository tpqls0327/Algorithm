# 3986 좋은 단어

ans = 0
for _ in range(int(input())):
    n = input()
    stack = []
    for i in n:
        if not stack:
            stack.append(i)
        else:
            stack.append(i)
            for j in range(int(len(stack)/2)):
                if stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
    if not stack:
        ans+=1
print(ans)
        
