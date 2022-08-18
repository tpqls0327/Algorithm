n, c = map(int, input().split())
arr = list(map(int, input().split()))
dic = {}

for i in range(n):
    if arr[i] in dic.keys():
        dic[arr[i]][0] += 1
    else:
        dic[arr[i]] = [1, i]
n_arr = sorted(dic.items(), key=lambda x: (-x[1][0], x[1][1]))
for i in n_arr:
    print(*[i[0]]*i[1][0], end=' ')
