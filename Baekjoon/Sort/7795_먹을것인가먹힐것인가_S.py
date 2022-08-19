# 7795 먹을 것인가 먹힐 것인가
import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

for _ in range(int(input())):
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    a.sort(reverse=True)
    b.sort()
    for i in a:
        tmp = bisect_left(b,i)
        ans+=tmp
    print(ans)
    
