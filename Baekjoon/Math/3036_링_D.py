from math import gcd    # 최대 공약수 함수

n = int(input())
arr = list(map(int, input().split()))

for i in range(1, n):
    g = gcd(arr[0], arr[i])
    print(f"{arr[0]//g}/{arr[i]//g}")
