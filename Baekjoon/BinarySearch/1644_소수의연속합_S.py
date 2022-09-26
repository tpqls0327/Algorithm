# 1644 소수의 연속합

import math

n = int(input())
arr = [False, False] + [True] * (n-1)
prime_arr = []

# 에라토스테네스의 체
for i in range(2, int(math.sqrt(n)) + 1):
    if arr[i]:
        j = 2
        while i * j <= n:
            arr[i * j] = False
            j += 1

for num in range(2, n + 1):
    if arr[num]:
        prime_arr.append(num)

# 경우의 수 구하기
end = 0
sum_num = 0
ans = 0
for start in prime_arr:
    while sum_num < n and end < len(prime_arr):
        sum_num += prime_arr[end]
        end += 1
    if sum_num == n:
        ans += 1
    sum_num -= start
print(ans)
