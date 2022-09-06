a, b = map(int, input().split())
arr = [0]
for i in range(1, 47):
    arr += [i] * i
print(sum(arr[a:b+1]))
