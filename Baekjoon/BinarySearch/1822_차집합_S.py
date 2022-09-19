# 1822 차집합

a,b = map(int, input().split())
arr = set(map(int, input().split()))
brr = set(map(int, input().split()))
ans = arr - brr
print(len(ans))

if ans:
    print(*sorted(ans))


