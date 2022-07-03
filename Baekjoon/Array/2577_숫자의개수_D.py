tmp = 1
for _ in range(3):
    tmp *= int(input())
tmp = list(str(tmp))

for i in range(10):
    print(tmp.count(str(i)))
