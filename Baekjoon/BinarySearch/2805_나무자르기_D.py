n, m = map(int, input().split())
height = list(map(int, input().split()))
s, e = 0, max(height)
ans = 0
while s <= e:
    mid = (s + e) // 2
    if sum([i - mid for i in height if i > mid]) >= m:
        ans = mid
        s = mid + 1
    else:
        e = mid - 1

print(ans)
