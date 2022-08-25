ans, stack, string = 0, [], input()
for i in range(len(string)):
    if string[i] == '(':
        stack.append('(')
    else:
        if string[i-1] == '(':
            stack.pop()
            ans += len(stack)
        else:
            stack.pop()
            ans += 1
print(ans)
