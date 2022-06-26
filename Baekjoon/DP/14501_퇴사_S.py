# 퇴사

n = int(input())
data = []
for i in range(n):
    t,p = map(int, input().split())
    data.append([t,p])

dp = [0 for i in range(n+1)]
for i in range(n-1, -1, -1):
    if data[i][0] + i <= n:
        dp[i] = max(data[i][1] + dp[i + data[i][0]], dp[i+1])
    else:
        dp[i] = dp[i+1]

print(dp[0])
            
