import sys
n = int(input())
arr = list(map(int, input().split()))

min_ = sys.maxsize
s, e = 0, n-1
min_s, min_e = 0, 0
while s < e:
    t = arr[s] + arr[e]

    if abs(t) < min_:
        min_s, min_e = s, e
        min_ = abs(t)

    if t > 0:
        e -= 1
    elif t < 0:
        s += 1
    else:
        break

print(arr[min_s], arr[min_e])
