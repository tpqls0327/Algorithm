n = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = [0]
for i in range(n):
    ans.append(ans[-1] + arr[i])
print(sum(ans))
