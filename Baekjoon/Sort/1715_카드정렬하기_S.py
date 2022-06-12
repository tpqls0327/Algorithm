# 카드 정렬하기

import sys
input = sys.stdin.readline
import queue

n = int(input())
q = queue.PriorityQueue()

for i in range(n):
    tmp = int(input())
    q.put(tmp)

result = 0
for i in range(n-1):

    if q == '':
        break
    else:
        cnt = q.get() + q.get()
        result += cnt
        q.put(cnt)
print(result)

    
