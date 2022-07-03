# 두수의 합
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
x = int(input())
data.sort()

result = 0
start, end = 0, n-1
while start < end:
    tmp = data[start] + data[end]
    if tmp == x:
        result += 1
        start += 1
    elif tmp > x:
        end -= 1
    else:
        start += 1
print(result)
