# 2910 빈도 정렬

n,c = map(int, input().split())
arr = list(map(int, input().split()))
data = []    # 데이터, 순서, 빈도 

cnt = 1
tmp_data = []
for a in arr:

    if not a in tmp_data:
        tmp_data.append(a)
        data.append([a,cnt,1])
        cnt += 1
    else:
        idx = tmp_data.index(a)
        data[idx][2] += 1

data.sort(key=lambda x: (-x[2],x[1]))
ans = []
for d in data:
    for i in range(d[2]):
        ans.append(d[0])
print(' '.join(str(a) for a in ans))
    
