m, n = map(int, input().split())
stick = list(map(int, input().split()))
s, e = 0, max(stick)
ans = 0
while s <= e:
    mid = (s + e) // 2
    if not mid:
        break
    if sum([i//mid for i in stick]) >= m:
        ans = mid
        s = mid + 1
    else:
        e = mid - 1
print(ans)
