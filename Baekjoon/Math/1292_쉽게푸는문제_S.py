# 쉽게푸는문제

a,b = map(int, input().split())
cnt = 1
arr = []
while True:
    for i in range(cnt):
        arr.append(cnt)
    cnt += 1
    if len(arr) > b:
        break
print(sum(arr[a-1:b]))
