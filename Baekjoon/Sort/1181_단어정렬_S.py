# 1181 단어 정렬

n = int(input())
arr = []
for i in range(n):
    arr.append(input())
set_arr = list(set(arr))

data = []
for i in set_arr:
    data.append((i,len(i)))
data.sort(key = lambda x:(x[1],x[0]))

for i in data:
    print(i[0])
