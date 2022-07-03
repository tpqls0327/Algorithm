# 방번호 

n = input()

data = [int(0) for _ in range(10)]

data69 = 0
for i in n:
    if i == '6' or i == '9':
        data69 += 1
    else:
        data[int(i)] += 1

result = max(max(data), (data69+1)/2)
print(int(result))
