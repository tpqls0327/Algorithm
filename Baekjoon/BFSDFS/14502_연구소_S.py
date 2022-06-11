# 연구소

from itertools import combinations
import copy
import sys
sys.setrecursionlimit(10**7)

# 입력 
n, m = map(int, input().split())
graph = []    # 지도 
maps = []     # 각 값들의 위치 
virus_list = []    # 2의 위치

for i in range(n):
    arr = list(map(int,input().split()))
    for j in range(len(arr)):
        if arr[j] == 2:
            virus_list.append((i,j))
        elif arr[j] == 0:
            maps.append((i,j))
    graph.append(arr)

data_list = list(combinations(maps,3))


dx = [-1,0,1,0]
dy = [0,1,0,-1]

# dfs로 바이러스가 퍼지게 하기
def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if tmp_maps[nx][ny] == 0:
                tmp_maps[nx][ny] = 2
                virus(nx,ny)

# 안전 영역의 크기
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if tmp_maps[i][j] == 0:
                score += 1
    return score

# 조합만큼 반복하며 2의 위치에서 dfs 실행
ans = 0
for data in data_list:
    tmp_maps = copy.deepcopy(graph)
    for x,y in data:
        tmp_maps[x][y] = 1
    for vx, vy in virus_list:
        if tmp_maps[vx][vy] == 2:
            virus(vx,vy)
    ans = max(ans, get_score())
print(ans)


