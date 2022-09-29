n, k = map(int, input().split())
arr = list(map(int, input().split()))

s, e = 0, 0
cnt = 1 if arr[0] % 2 else 0
ans = 0 if arr[0] % 2 else 1

while e < n-1:
    e += 1

    if arr[e] % 2:
        cnt += 1

        while cnt > k:
            if arr[s] % 2:
                cnt -= 1
            s += 1

    ans = max(ans, e-s+1-cnt)

print(ans)
