from collections import deque
import sys

# input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]


# 섬 번호 추가해주는 함수(1~n)
def countries(i, j):
    q = deque([[i, j]])

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny]:
                board[nx][ny] = c_cnt
                visited[nx][ny] = 1
                q.append([nx, ny])


# 가까운 거리의 섬 찾는 함수
def bfs(q, cnt):
    while q:
        x, y, z = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < n and 0 <= ny < n:
                if not ways[nx][ny] and not board[nx][ny]:  # 아직 방문하지 않은 바다
                    ways[nx][ny] = 1
                    q.append([nx, ny, z+1])     # 최소거리가 보장되므로 +1씩
                elif visited[nx][ny] and board[nx][ny] and board[nx][ny] != cnt:
                    return z        # 다른 섬을 만났다면 즉시 중지 및 반환


c_cnt = 1   # 섬 번호
for i in range(n):
    for j in range(n):
        if not visited[i][j] and board[i][j]:
            board[i][j] = c_cnt
            visited[i][j] = 1
            countries(i, j)
            c_cnt += 1

ans = int(1e9)  # 가장 가까운 거리
for c in range(1, c_cnt):
    que = deque()
    ways = [[0] * n for _ in range(n)]  # 0 순회할 visited 배열

    for i in range(n):
        for j in range(n):
            if board[i][j] == c:
                ways[i][j] = 1
                que.append([i, j, 0])
    ans = min(bfs(que, c), ans)

print(ans)
