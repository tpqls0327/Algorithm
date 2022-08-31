# 1541 잃어버린 괄호
import re

n = input()
data = re.split('\W+',n)
pattern = re.split(r'[0-9]',n)
pattern = list(filter(None, pattern))

pdx = 0    # 괄호 인덱스
for p in pattern:
    if pattern[pdx] == '+':
        data[0] = int(data[0]) + int(data[1])
        del data[1]
        pdx += 1
    else: break

ans = int(data[0])
for i in range(1,len(data)):
    ans -= int(data[i])
print(ans)



# 다른사람 코드
arr = input().split('-')
s = 0
for i in arr[0].split('+'):
    s += int(i)
for i in arr[1:]:
    for j in i.split('+'):
        s -= int(j)
print(s)
