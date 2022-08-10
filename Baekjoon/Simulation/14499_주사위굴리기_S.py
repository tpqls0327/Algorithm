# 14499 주사위 굴리기

n,m,x,y,k = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
move = list(map(int, input().split()))
dice = [0,0,0,0,0,0]   # 1,2,3,4,5,6 | 상앞우좌뒤하
dx,dy = (0,0,-1,1), (1,-1,0,0) # 동서북남
dice_direct = {1:[3,1,0,5,4,2], 2:[2,1,5,0,4,3], 3:[4,0,2,3,5,1], 4:[1,5,2,3,0,4]} # 동서북남 이동 좌표

def check(nx,ny):
    if arr[nx][ny] == 0:
        arr[nx][ny] = dice[-1]      
    else:
        dice[-1] = arr[nx][ny]
        arr[nx][ny] = 0
    
def rolling(idx):
    global x,y,dice
    tmp_dice = [-1,-1,-1,-1,-1,-1]
    num = dice_direct[idx]
    nx,ny = x+dx[idx-1], y+dy[idx-1]
    if nx >= 0 and nx < n and ny >= 0 and ny < m:
        x = nx
        y = ny
        for rdx, r_num in enumerate(num):
            tmp_dice[rdx] = dice[r_num]
        dice = tmp_dice
        check(nx,ny)
    else:
        return False
    return True
            
for idx in move:
    if rolling(idx):
       print(dice[0])     
