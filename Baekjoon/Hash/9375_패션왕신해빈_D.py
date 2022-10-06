from collections import defaultdict

for _ in range(int(input())):
    dic = defaultdict(list)
    for _ in range(int(input())):
        c, t = input().split()
        dic[t].append(c)
    cnt = 1
    for c in dic:
        cnt *= (len(dic[c]) + 1)
    print(cnt-1)
