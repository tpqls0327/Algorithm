def fact(k, p):
    c = 0
    while k:
        k //= p
        c += k
    return c


n, m = map(int, input().split())
print(min(fact(n, 2)-fact(n-m, 2)-fact(m, 2), fact(n, 5)-fact(n-m, 5)-fact(m, 5)))
