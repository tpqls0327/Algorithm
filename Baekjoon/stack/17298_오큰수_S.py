# 오큰수

n = int(input())
arr = list(map(int,input().split()))

cnt = [-1] * n
stack = []

for i in range(n):
    while stack and (stack[-1][0] < arr[i]):
        tmp, idx = stack.pop()
        cnt[idx] = arr[i]
    stack.append([arr[i], i])
print(*cnt)
