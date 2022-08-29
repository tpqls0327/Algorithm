#11399 ATM

n = int(input())
p = list(map(int, input().split()))

p.sort()
ans = 0
cnt = 0
for i in p:
    cnt += i
    ans += cnt
print(ans)
