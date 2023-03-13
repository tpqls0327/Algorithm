import sys

n, m = map(int, input().split())
dic = {}

for _ in range(n):
    e, p = sys.stdin.readline().split()
    dic[e] = p

for _ in range(m):
    print(dic[sys.stdin.readline().rstrip()])
