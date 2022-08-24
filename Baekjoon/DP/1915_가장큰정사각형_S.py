# 1915 가장 큰 정사각형

n,m = map(int, input().split())
dp = [list(input()) for _ in range(n)]
for i in range(n):
    dp[i] = list(map(int, dp[i]))

for i in range(1, n):
    for j in range(1, m):
        if dp[i][j] == 1:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
ans = 0
for i in dp:
    ans = max(ans, max(i))
print(ans*ans)
