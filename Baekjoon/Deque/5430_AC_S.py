# 5430 AC

from collections import deque
import sys
input = sys.stdin.readline

for i in range(int(input())):
    arr = input().rstrip()
    n = int(input())
    num = input().rstrip()
    if num != '[]':
        q = deque(map(int, num[1:len(num)-1].split(',')))
    else: q = deque()
    
    cnt = 0
    r_cnt = 0   # R이 나온 횟수
    for a in arr:
        if a == 'R': 
             r_cnt += 1
        else:
            if len(q) == 0:
                print('error')
                cnt = 1
                break
            else:
                if r_cnt %2 == 0:
                    q.popleft()
                else: q.pop()
    if r_cnt % 2 == 1:
        q.reverse()
    if cnt == 0:
        print("[" + ','.join(map(str, q)) + "]")
    cnt = 0
