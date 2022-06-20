# 정수 삼각형

n = int(input())
data = []

for i in range(n):
    arr = list(map(int, input().split()))
    data.append(arr)

for i in range(1, n):
    for j in range(i+1):
 
        # 왼
        if j == 0:
            left = 0
        else:
            left = data[i-1][j-1]

        # 우
        if j == i:
            right = 0
        else:
            right = data[i-1][j]
            
        data[i][j] = data[i][j] + max(left, right)

print(max(data[-1][:]))
