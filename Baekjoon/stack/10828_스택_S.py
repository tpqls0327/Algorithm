# 스택

import sys
input = sys.stdin.readline

n = int(input())

stack = []
for _ in range(n):
    commend = input().split()

    if commend[0] == 'push':
        stack.append(commend[1])
    elif commend[0] == 'top':
        if not stack:
            print('-1')
        else:
            print(stack[-1])
    elif commend[0] == 'size':
        print(len(stack))
    elif commend[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else: print(0)
    elif commend[0] == 'pop':
        if len(stack) == 0:
            print('-1')
        else:
            print(stack.pop())
        
        
