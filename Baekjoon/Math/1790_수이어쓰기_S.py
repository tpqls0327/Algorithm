# 1790 수이어쓰기2

n,k = map(int, input().split())
num = 9
cnt = 1
ans = 0   # 수의 길이

while k > (cnt * num):
    k -= cnt * num
    ans += num
    num = num * 10
    cnt += 1

ans = (ans+1) + (k-1) // cnt

if ans < cnt:
    print(-1)
else:
    print(str(ans)[(k-1)%cnt])

