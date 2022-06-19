# 금광

t = int(input())

for _ in range(t):
    n,m = map(int, input().split())
    arr = []
    tmp = list(map(int, input().split()))

    for i in range(0,len(tmp), m):
        arr.append(tmp[i:i+m])

    for i in range(1, m):
        for j in range(n):
            if j == 0:
                left_up = 0
            else:
                left_up = arr[j-1][i-1]

            if j == n - 1:
                left_down = 0
            else:
                left_down = arr[j+1][i-1]

            left = arr[j][i-1]
            arr[j][i]  = arr[j][i] + max(left_up, left_down, left)
            
    result = 0
    for i in range(n):
        result = max(result, arr[i][m-1])
       
    print(result)
        
                

    
        
    
    
    
