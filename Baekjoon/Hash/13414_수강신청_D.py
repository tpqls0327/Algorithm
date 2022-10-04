import sys

k, l = map(int, input().split())
dic = {sys.stdin.readline().rstrip(): i for i in range(l)}

for i, j in sorted(dic.items(), key=lambda x: x[1])[:k]:
    print(i)
