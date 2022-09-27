# 2003 수들의 합 2

n,m = map(int, input().split())
arr = list(map(int, input().split()))

end = 0
sum_num = 0
ans = 0
for start in arr:
    while sum_num < m and end < len(arr):
        sum_num += arr[end]
        end += 1
    if sum_num == m:
        ans += 1
    sum_num -= start
print(ans)
