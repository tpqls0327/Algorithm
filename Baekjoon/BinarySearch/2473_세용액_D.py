import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
a.sort()
min_ = sys.maxsize
min_i, min_s, min_e = 0, 0, 0

for i in range(n-2):
    s, e = i + 1, n - 1

    while s < e:
        t = a[i] + a[s] + a[e]

        if abs(t) < min_:
            min_i, min_s, min_e = i, s, e
            min_ = abs(t)

        if t < 0:
            s += 1
        elif t > 0:
            e -= 1
        else:
            print(a[min_i], a[min_s], a[min_e])
            exit(0)

print(a[min_i], a[min_s], a[min_e])
