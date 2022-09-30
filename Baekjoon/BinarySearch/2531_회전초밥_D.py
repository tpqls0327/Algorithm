from collections import defaultdict

n, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
dic = defaultdict(int, {c: 1})
s, e = 0, 0
ans = 0

while e < k:
    dic[arr[e]] += 1
    e += 1

while s < n:
    ans = max(ans, len(dic))
    dic[arr[s]] -= 1
    if not dic[arr[s]]:
        del dic[arr[s]]
    dic[arr[e]] += 1
    s += 1
    e += 1

print(ans)
