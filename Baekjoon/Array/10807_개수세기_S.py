# 개수세기

n = int(input())
data = list(map(int, input().split()))
v = int(input())

result = 0
for i in data:
    if i == v:
        result+=1
print(result)
