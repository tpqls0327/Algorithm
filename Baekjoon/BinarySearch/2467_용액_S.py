# 2467 용액
import sys

n = int(input())
arr = list(map(int, input().split()))

def binary_search(data):
    start, end = 0, n-1
    ans = sys.maxsize
    
    while start < end:
        if arr[start] + arr[end] == 0:
            return print(arr[start],arr[end])
        
        elif arr[start] + arr[end] < 0:
            if abs(arr[start] + arr[end]) < ans:
                pre_start = start
                pre_end = end
                ans = abs(arr[start] + arr[end])
            start += 1
            
        elif arr[start] + arr[end] > 0:
            if abs(arr[start] + arr[end]) < ans:
                pre_start = start
                pre_end = end
                ans = abs(arr[start] + arr[end])
            end -= 1
            
    return print(arr[pre_start],arr[pre_end])

binary_search(arr)
