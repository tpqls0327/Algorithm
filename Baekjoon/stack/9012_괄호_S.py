#9012 괄호

def vps(n):
    stack = []
    for i in n:
        if not stack:
            if i == ')':
                return 'NO'
            else: stack.append(i)
        else:
            if i == ')':
                if stack[-1] == '(':
                    stack.pop()
            else: stack.append(i)
    if stack:
       return 'NO'
    else: return 'YES'

for _ in range(int(input())):
    print(vps(input()))
