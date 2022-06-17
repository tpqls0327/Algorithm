# 고정점 찾기 2022-06-13

from bisect import bisect_left, bisect_right

n = int(input())
data = list(map(int, input().split()))

result = ''
for i in range(n):
    start = i
    end = n-i-1
    
    if start == data[start]:
        result = data[start]
        break
    elif end == data[end]:
        result = data[end]
        break
    
if result == '':
    print('-1')
else:
    print(result)
