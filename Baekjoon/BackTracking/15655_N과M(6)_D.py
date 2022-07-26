n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
s = []


def back(k):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(k, n):
        if arr[i] not in s:
            s.append(arr[i])
            back(i)
            s.pop()


back(0)
