import sys
input = sys.stdin.readline

n = int(input())
arr = []
a_app = arr.append
for i in range(n):
    name, kor, eng, math = input().split()
    a_app([name, int(kor), int(eng), int(math)])

arr = sorted(arr, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in arr:
    print(i[0])
