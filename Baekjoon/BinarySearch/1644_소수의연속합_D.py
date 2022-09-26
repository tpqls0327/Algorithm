def sosu(x):
    for i in range(2, int(x**0.5)+1):
        if not x % i:
            return False
    return n


n = int(input())

arr = [i for i in range(2, n+1) if sosu(i)]
cnt = 0

n_arr = len(arr)
s, e = 0, 0
while e <= n_arr:
    t = sum(arr[s:e])
    if t < n:
        e += 1
    elif t > n:
        s += 1
    else:
        cnt += 1
        e += 1

print(cnt)
