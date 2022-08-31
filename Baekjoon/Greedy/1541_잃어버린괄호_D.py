arr = input()
ans, tmp, once = '', '', False
for a in arr:
    if a == '+':
        ans += (str(int(tmp)) + '-') if once else (str(int(tmp)) + '+')
        tmp = ''
    elif a == '-':
        ans += (str(int(tmp)) + '-')
        tmp = ''
        once = True
    else:
        tmp += a

if tmp:
    ans += str(int(tmp))

print(eval(ans))

# 더 간단한 코드
# arr = input().split('-')
# s = 0
# for i in arr[0].split('+'):
#     s += int(i)
# for i in arr[1:]:
#     for j in i.split('+'):
#         s -= int(j)
# print(s)
