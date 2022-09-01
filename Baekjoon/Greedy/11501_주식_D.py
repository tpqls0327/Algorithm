for _ in range(int(input())):
    n = int(input())
    stocks = list(map(int, input().split()))
    ans = 0
    _max = stocks[-1]
    for i in range(n-1, -1, -1):
        if stocks[i] <= _max:
            ans += (_max - stocks[i])
        else:
            _max = stocks[i]
    print(ans)
