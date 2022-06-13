n = int(input())
arr = list(map(int, input().split()))

def loof(start, end):
    mid = (start+end) // 2
    
    if start+1 == end:
        return mid if arr[mid] == mid else -1
    
    if arr[mid] > mid:
        return loof(start, mid)
    elif arr[mid] < mid:
        return loof(mid, end)
    else:
        return mid
    
print(loof(0, n-1))


# 정답 코드

def bi(start, end):
    if start > end:
        return None
    mid = (start+end)//2
    
    if arr[mid] > mid:
        return bi(start, mid-1)
    elif arr[mid] < mid:
        return bi(mid+1, end)
    else:
        return mid
    
    
n = int(input())
arr = list(map(int, input().split()))
idx = bi(0, n-1)

print(idx if idx else -1)
