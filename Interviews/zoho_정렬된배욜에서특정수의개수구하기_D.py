n, x = map(int, input().split())
arr = list(map(int, input().split()))

min_ = n
max_ = 0
for i in range(n//2+1):
    if arr[i] == x:
        min_ = min(min_, i)
    if arr[n-1-i] == x:
        max_ = max(max_, n-1-i)
        
if min_ == n and max_ == 0:
    print(-1)
else:
    print(max_ - min_ + 1)


# bisect 이용 풀이
from bisect import bisect_left, bisect_right


n, x = map(int, input().split())
arr = list(map(int, input().split()))

left = bisect_left(arr, x)
right = bisect_right(arr, x)

result = right - left
if result == 0:
    print("-1")
else:
    print(result)