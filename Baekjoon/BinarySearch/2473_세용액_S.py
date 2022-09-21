# 2473 세 용액
import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
ans = sys.maxsize 
result = []
cnt = 0

for i in range(n-2):
    mid = arr[i]
    start = i+1
    end = n-1
    
    while start < end:
        data = mid + arr[start] + arr[end]
        if abs(data) <= abs(ans): 
            result = [mid, arr[start], arr[end]] 
            ans = mid + arr[start] + arr[end] 
        if data < 0:
            start += 1
        elif data > 0:
            end -= 1
        else:
            print(*result)
            sys.exit()

print(*result)

