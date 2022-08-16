# 5648 역원소 정렬

cnt = 0
n = list(map(int,input().split()))
cnt = len(n) -1
num = n[0]
del n[0]

while True:
    tmp = list(m1ap(int, input().split()))
    cnt += len(tmp)
    for i in range(len(tmp)):
        n.append(tmp[i])
    if cnt >= num:
        break

answer = []
for i in range(len(n)):
    a = list(str(n[i]))
    a = a[::-1]
    ans = int(''.join(a))
    answer.append(ans)
answer.sort()
for i in answer:
    print(i)
