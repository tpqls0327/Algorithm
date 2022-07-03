n, k = map(int, input().split())
room = [[0, 0] for _ in range(7)]

for _ in range(n):
    s, y = map(int, input().split())
    room[y][s] += 1

cnt = 0

for i, j in room:
    cnt += (i//k+1) if i % k else (i//k)
    cnt += (j//k+1) if j % k else (j//k)

print(cnt)