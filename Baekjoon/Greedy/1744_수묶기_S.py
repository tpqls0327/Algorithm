# 1744 수 묶기

n = int(input())
arr = []
reverse_arr = []
zero = 0   # 0: 제로가 있음 1: 제로가 없음

for _ in range(n):
    tmp = int(input())
    if tmp < 0: reverse_arr.append(tmp)
    elif tmp > 0: arr.append(tmp)
    else: zero = 1
    
arr.sort()
reverse_arr.sort(reverse=True)

# 양수 확인
ans = 0
for i in range(len(arr)-1,-1,-2):
    if i == 0: ans += arr[i]
    else:
        if arr[i] == 1 or arr[i-1] == 1:
            ans += arr[i] + arr[i-1]
        else:
            ans += arr[i] * arr[i-1]
        
# 음수 확인
for i in range(len(reverse_arr)-1,-1,-2):
    if i == 0:
        if not zero:
            ans += reverse_arr[i]
    else:
        ans += reverse_arr[i] * reverse_arr[i-1]
print(ans)

