# N과M(6)

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
temp = []

def back(start):
    if len(temp) == m:
        print(*temp)
        return
    for i in range(start, n):
        if nums[i] not in temp:
            temp.append(nums[i])
            back(i + 1)
            temp.pop()

back(0)
