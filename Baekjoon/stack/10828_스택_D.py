import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    tmp = input().split()
    if tmp[0] == 'push':
        arr.append(int(tmp[1]))
    elif tmp[0] == 'pop':
        print(arr.pop() if arr else -1)
    elif tmp[0] == 'top':
        print(arr[-1] if arr else -1)
    elif tmp[0] == 'size':
        print(len(arr))
    elif tmp[0] == 'empty':
        print(0 if arr else 1)
