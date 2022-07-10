# 요세푸스 문제

n, k = map(int,input().split())
arr = [i for i in range(1,n+1)]

answer = []
num = 0
while len(answer) != n:
    num = (num + (k-1)) % len(arr)
    answer.append(arr.pop(num))
print("<%s>" % (", ".join(map(str,answer))))
