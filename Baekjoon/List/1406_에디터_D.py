import sys
input = sys.stdin.readline

arr = list(input().rstrip())
tmp = []
n = int(input())
for _ in range(n):
    cmd = input().rstrip()
    if arr and cmd == 'L':
        tmp.append(arr.pop())
    elif tmp and cmd == 'D':
        arr.append(tmp.pop())
    elif arr and cmd == 'B':
        arr.pop()
    elif cmd[0] == 'P':
        arr.append(cmd[2])

while tmp:
    arr.append(tmp.pop())
print(''.join(arr))
