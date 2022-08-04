from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    order = input().rstrip()
    n = int(input())
    arr = deque(input().rstrip()[1:-1].split(',')) if n else deque(input().rstrip()[1:-1])

    err, rev = 1, 0

    for i in order:
        if i == 'R':
            rev += 1
        else:
            if arr:
                arr.pop() if rev % 2 else arr.popleft()
            else:
                err = 0
                break

    if err:
        if rev % 2:
            arr.reverse()
        print(f"[{','.join(arr)}]")
    else:
        print("error")
