# 11501 주식
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    max_num = arr[-1]
    
    ans = 0
    for a in arr[::-1]:
        if a > max_num: max_num = a
        else: ans += max_num - a        
    print(ans)
