def rev(array):
    return [int(a[::-1]) for a in array]


n, *arr = list(input().split())
arr = rev(arr)

while len(arr) < int(n):
    arr += rev(list(input().split()))
for i in sorted(arr):
    print(i)
