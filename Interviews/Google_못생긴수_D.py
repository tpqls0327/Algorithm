n = int(input())
dp = [0 for _ in range(1001)]
dp[1] = 1

for i in range(2, 1001):
    if (not i % 2 or not i % 3 or not i % 5) and i % 7:
        dp[i] = 1
        
ans = [i for i in range(1001) if dp[i]]

print(ans[n-1])
