# 1941 소문난 칠공주
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000000)

def check_range(y, x):
    return (0 <= y < 5) and (0 <= x < 5)

def dfs(data, S, Y):
    global answer, visited
    if Y > 3:
        return
    
    if len(data) == 7 and S >= 4:
        data = tuple(sorted(data))
        if data not in visited:
            visited.add(data)
            answer += 1
        return
    
    for pos in data:
        y = pos//5
        x = pos%5
        dy = [1, -1, 0, 0]
        dx = [0, 0, 1, -1]
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            n = ny * 5 + nx
            if check_range(ny, nx) and n not in data:
                data.append(n)
                if graph[ny][nx] == 'Y':
                    dfs(data, S, Y+1)
                else:
                    dfs(data, S+1, Y)
                data.pop()

graph = [list(input()) for _ in range(5)]
answer = 0
visited = set()
for i in range(5):
    for j in range(5):
        if graph[i][j] == 'S':
            data = []
            data.append(i * 5 + j)
            dfs(data, 1, 0)
print(answer)
