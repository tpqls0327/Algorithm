import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort(reverse=True)
    b.sort(reverse=True)
    i, j = 0, 0
    ans = 0
    while True:
        if i >= n or j >= m:
            break
        if a[i] > b[j]:
            ans += (m-j)
        else:
            j += 1
            i -= 1
        i += 1
    print(ans)
