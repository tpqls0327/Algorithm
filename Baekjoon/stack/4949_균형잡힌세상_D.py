def trace(string):
    stack = []
    for s in string:
        if s in ['(', '[']:
            stack.append(s)
        elif s == ')':
            if not stack or stack.pop() != '(':
                return False
        elif s == ']':
            if not stack or stack.pop() != '[':
                return False

    return False if stack else True


while True:
    string = input()
    if string == '.':
        break
    print('yes') if trace(string) else print('no')
