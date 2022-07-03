n = int(input())
arr = list(map(int, input().split()))
arr.sort()
x = int(input())
cnt, i, j = 0, 0, n-1

while i != j:
    if arr[i]+arr[j] == x:
        cnt += 1
        i += 1
    elif arr[i]+arr[j] > x:
        j -= 1
    else:
        i += 1

print(cnt)