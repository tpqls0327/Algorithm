for _ in range(int(input())):
    n, m = map(int, input().split())
    gold_map = []

    tmp = list(map(int, input().split()))
    for i in range(n):
        gold_map.append(tmp[i*m:i*m+m])

    for i in range(1, m):
        for j in range(n):
            if j == 0:
                lu = 0
            else:
                lu = gold_map[j - 1][i - 1]

            if j == n-1:
                ld = 0
            else:
                ld = gold_map[j + 1][i - 1]

            l = gold_map[j][i-1]
            gold_map[j][i] = gold_map[j][i] + max(lu, ld, l)

    ans = 0
    for i in range(n):
        ans = max(ans, gold_map[i][m-1])
    print(ans)


# 2
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
