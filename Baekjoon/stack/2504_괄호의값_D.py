string = input()
stack, answer, tmp = [], 0, 1

for i in range(len(string)):
    if string[i] == '(':
        stack.append('(')
        tmp *= 2
    elif string[i] == '[':
        stack.append('[')
        tmp *= 3
    elif string[i] == ')':
        if not stack or stack[-1] == '[':
            answer = 0
            break
        if string[i-1] == '(':
            answer += tmp
        stack.pop()
        tmp //= 2
    else:
        if not stack or stack[-1] == '(':
            answer = 0
            break
        if string[i-1] == '[':
            answer += tmp
        stack.pop()
        tmp //= 3

print(0) if stack else print(answer)
