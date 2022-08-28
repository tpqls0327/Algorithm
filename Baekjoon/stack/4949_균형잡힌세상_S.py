# 4949 균형잡힌 세상

def bracket(n):
    stack = []
    for i in n:
        if i == '(' or i == ')' or i == '[' or i == ']':
            if not stack:
                if i == ')' or i == ']': return 'no'
            if i == ')':
                if stack[-1] != '(': return 'no'
                else: stack.pop()
            elif i == ']':
                if stack[-1] != '[':
                    return 'no'
                else: stack.pop()
            else: stack.append(i)
    if not stack:
        return 'yes'
    else: return 'no'
                

while True:
    n = input()
    if n == '.':
        break
    print(bracket(n))
