n = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans, cnt = 0, [0] * 40001

for i in range(n):
    ans += cnt[20000 - arr[i]]
    for j in range(i):
        cnt[20000 + arr[i] + arr[j]] += 1

print(ans)
