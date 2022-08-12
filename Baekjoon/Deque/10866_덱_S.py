# 10866 덱

from collections import deque
import sys
input = sys.stdin.readline

q = deque()
for i in range(int(input())):
    data = input().split()
    if data[0] == 'push_front':
        q.appendleft(data[1])
    elif data[0] == 'push_back':
        q.append(data[1])
    elif data[0] == 'pop_front':
        if len(q) == 0:
            print(-1)
        else:
            n = q.popleft()
            print(n)
    elif data[0] == 'pop_back':
        if len(q) == 0:
            print(-1)
        else:
            n = q.pop()
            print(n)
    elif data[0] == 'size':
        print(len(q))
    elif data[0] == 'empty':
        if len(q) == 0:
            print(1)
        else: print(0)
    elif data[0] == 'front':
        if len(q) == 0:
            print(-1)
        else: print(q[0])
    elif data[0] == 'back':
        if len(q) == 0:
            print(-1)
        else: print(q[-1])
