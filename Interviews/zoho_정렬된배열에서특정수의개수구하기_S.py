# 정렬된 배열에서 특정 수의 개수 구하기

# 이진탐색 메소드 직접 구
n, x = map(int, input().split())
data = list(map(int, input().split()))
    
def binary_search(data, x, start, end):
    result = [0,0]

    while start <= end:
        if data[start] == x:
            if result[0] == 0:
                result[0] = start
            start += 1
        else:
            start += 1
            
        if data[end] == x:
            if result[1] == 0:
                result[1] = end
            end -= 1
        else:
            end -= 1
    return result
        
answer = binary_search(data, x, 0, n-1)
if answer[0] == 0 and answer[1] == 0:
    print('-1')
else:
    print(answer[1] - answer[0] + 1)
            




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
