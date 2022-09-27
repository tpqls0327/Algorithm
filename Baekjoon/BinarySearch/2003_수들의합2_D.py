n, m = map(int, input().split())
arr = list(map(int, input().split()))

s, e = 0, 0
cnt = 0
while e <= n:
    mid = sum(arr[s:e])

    if mid > m:
        s += 1
    elif mid < m:
        e += 1
    else:
        cnt += 1
        e += 1

print(cnt)
