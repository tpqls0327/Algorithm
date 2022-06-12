from queue import PriorityQueue

n = int(input())
que = PriorityQueue(n)
for i in range(n):
    que.put(int(input()))
result = 0

while que.qsize() > 1:
    a = que.get()
    b = que.get()
    result += (a+b)
    que.put(a+b)

print(result)
