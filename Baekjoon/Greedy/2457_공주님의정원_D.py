n = int(input())
flowers = []

for _ in range(n):
    sm, sd, em, ed = map(int, input().split())
    flowers.append([sm*100+sd, em*100+ed])

t = 301
ans = 0
while t < 1201:
    nxt = t
    for i in range(n):
        if flowers[i][0] <= t and flowers[i][1] > nxt:
            nxt = flowers[i][1]
    if nxt == t:
        print(0)
        exit(0)
    ans += 1
    t = nxt

print(ans)
