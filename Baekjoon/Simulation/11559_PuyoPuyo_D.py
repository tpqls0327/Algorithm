from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]       # bfs 회전용
r, c, dot = 6, 12, '.'      # (회전된) 가로, 세로, 자주 나오는 값 변수 정의
board = deque([deque(['']*c) for _ in range(r)])
for n in range(c):
    t = input()
    for m in range(r):
        board[m][n] = t[r-1-m]


def put_back():     # 빈 공간 없애는 함수
    for row in range(r):
        if board[row].count(dot) == c:  # 바꿀 필요 없는 경우 pass
            continue
        tmp_arr = deque([board[row][qt] for qt in range(c) if board[row][qt] != dot])   # .이 아닌 것들만 추출

        for qt in range(c-len(tmp_arr)):    # 추출된 배열 앞쪽(왼쪽)에 가로 갯수 동일할 때까지 추가
            tmp_arr.appendleft(dot)
        board[row] = tmp_arr        # 값 덮어 씌우기


def bfs():
    is_boom = False
    visited = [[0]*c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if board[i][j] != dot and not visited[i][j]:
                q = deque([[i, j]])
                visited[i][j] = 1
                same_color = [[i, j]]   # 같은 색상 위치
                while q:
                    x, y = q.pop()

                    for p in range(4):
                        nx, ny = x + dx[p], y + dy[p]

                        if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and board[i][j] == board[nx][ny]:
                            same_color.append([nx, ny])
                            q.append([nx, ny])
                            visited[nx][ny] = 1

                if len(same_color) >= 4:
                    for a, b in same_color:
                        board[a][b] = dot   # 일단 해당 위치를 .으로 변경
                    is_boom = True          # 재정렬 후 반복을 위해
                # print(same_color)
    return is_boom


t_cnt = 0           # 최종값
while True:
    if bfs():
        t_cnt += 1
        put_back()
    else:
        break

    # for o in board:
    #     print(o)
print(t_cnt)
