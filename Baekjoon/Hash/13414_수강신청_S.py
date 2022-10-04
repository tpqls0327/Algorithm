# 13414 수강신청
import sys
input = sys.stdin.readline

k,l = map(int, input().split())
arr = {}

for i in range(l):
    tmp = input().rstrip()
    arr[tmp] = i

sorted_arr = dict(map(reversed, arr.items()))
print(sorted_arr)

cnt = 0
for i in range(l):
    if i in sorted_arr:
        print(sorted_arr[i])         
        cnt += 1
    else: continue
    if cnt == k: break
