# 18428 감시 피하기 

import itertools
import copy

n = int(input())
arr = []
for i in range(n):
    tmp = list(input().split())
    arr.append(tmp)

teacher = []
empty = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'T':
            teacher.append((i,j))
        elif arr[i][j] == 'X':
            empty.append((i,j))

nx = [-1,1,0,0]
ny = [0,0,-1,1]

def bfs(arr):
    for t in teacher:
        for i in range(4):
            bx = t[0] + nx[i]
            by = t[1] + ny[i]
                
            while True:
                if bx <= -1 or bx >= n or by <= -1 or by >= n:
                    break
                if arr[bx][by] == 'S':
                    return False
                elif arr[bx][by] == 'O':
                    break
                else:
                    bx = bx + nx[i]
                    by = by + ny[i]
    return True


result = 'NO'
for x in itertools.combinations(empty, 3):
    tmp_arr = copy.deepcopy(arr)
    
    # 벽 세우기
    for data in x:
        tmp_arr[data[0]][data[1]] = 'O'
    if bfs(tmp_arr) == True:
        result = 'YES'
    if result == 'YES':
        break
print(result) 

        
        
