import sys
input = sys.stdin.readline

arr = []
for _ in range(int(input())):
    t = int(input())
    arr.append(t) if t else arr.pop()
print(sum(arr))
