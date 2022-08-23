# 9084 동전

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    money = int(input())
    arr.insert(0,0)

    dp = [[0] * (money+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    
    for i in range(1,n+1):
        for j in range(1,money+1):
            dp[i][j] = dp[i-1][j]
            if j-arr[i] >= 0:
                dp[i][j] += dp[i][j-arr[i]]
    print(dp[-1][-1])
