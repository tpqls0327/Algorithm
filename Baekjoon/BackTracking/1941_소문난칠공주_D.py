def permu(idx, ans, position):
    global cnt, check
    print(ans)
    if ans.count('Y') > 3:
        return
    if idx == 7:
        if ans.count('S') >= 4:
            position_check(position[0], position)
            if sum(sum(check, [])) == 7:
                cnt += 1
            check = [[0] * 5 for _ in range(5)]
        return
    for i in range(25):
        if not visit[i]:
            visit[i] = 1
            permu(idx+1, ans+arr[i], position+[i])
            for j in range(i+1, 25):
                visit[j] = 0


def position_check(s, position):
    x = s // 5
    y = s % 5
    check[x][y] = 1
    for j in range(4):
        nx = x + dx[j]
        ny = y + dy[j]
        if 0 <= nx < 5 and 0 <= ny < 5:
            next_ = nx * 5 + ny
            if not check[nx][ny] and next_ in position:
                check[nx][ny] = 1
                position_check(next_, position)


arr = []
for _ in range(5):
    arr += list(input())
cnt = 0
visit = [0 for _ in range(25)]
check = [[0] * 5 for _ in range(5)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
permu(0, '', [])
print(cnt)
