from collections import deque
import sys
q = deque()
input = sys.stdin.readline
for _ in range(int(input())):
    op = input().split()

    if op[0] == 'push_front':
        q.appendleft(op[1])
    elif op[0] == 'push_back':
        q.append(op[1])
    elif op[0] == 'pop_front':
        print(q.popleft() if q else -1)
    elif op[0] == 'pop_back':
        print(q.pop() if q else -1)
    elif op[0] == 'size':
        print(len(q))
    elif op[0] == 'empty':
        print(0 if q else 1)
    elif op[0] == 'front':
        print(q[0] if q else -1)
    elif op[0] == 'back':
        print(q[-1] if q else -1)
