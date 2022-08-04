def back(a):
    global k, arr, s
    if len(s) == 6:
        print(' '.join(map(str, s)))
        return

    for i in range(a, k):
        if arr[i] not in s:
            s.append(arr[i])
            back(i)
            s.pop()


while True:
    s = []
    k, *arr = map(int, input().split())
    if not k:
        break
    back(0)
    print()
