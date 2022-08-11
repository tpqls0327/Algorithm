from collections import deque

n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

que = deque([[trucks[0], w]])
time, pos, is_last = 1, 1, False    # 걸린 시간, 트럭 번호, 마지막 트럭 확인용
while que:
    # print(time, que)
    time += 1
    w_total = 0
    tmp = deque()
    while que:
        x, y = que.popleft()
        if y-1 > 0:
            w_total += x
            tmp.append([x, y-1])

    if pos < n and w_total + trucks[pos] <= L and not is_last:
        if pos == n:
            is_last = True
        elif pos < n:
            tmp.append([trucks[pos], w])
        pos += 1
    que = tmp

print(time)
