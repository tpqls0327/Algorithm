def trace(string):
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        else:
            if not stack or stack.pop() != '(':
                return False
    return False if stack else True


for _ in range(int(input())):
    print('YES') if trace(input()) else print('NO')
