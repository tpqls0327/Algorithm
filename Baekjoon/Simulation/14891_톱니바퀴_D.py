from collections import deque

nee = deque()
for _ in range(4):
    tmp = deque(map(int, list(input())))
    nee.append(tmp)


# 톱니 번호, 방향, 이전의 움직임
def check(num, arw):
    global move_check

    if arw > 0:
        if num >= 3:
            return
        if nee[num][2] != nee[num+arw][6]:
            if move_check[num]:
                move_check[num+arw] = True
                return check(num+arw, arw)
    else:
        if num <= 0:
            return
        if nee[num][6] != nee[num+arw][2]:
            if move_check[num]:
                move_check[num+arw] = True
                return check(num+arw, arw)


k = int(input())
for _ in range(k):
    pos, arrow = map(int, input().split())
    pos -= 1

    move_check = [False] * 4
    move_check[pos] = True

    check(pos, 1)
    check(pos, -1)
    tp = arrow
    for q in range(pos, 4):
        if move_check[q]:
            nee[q].rotate(tp)
            tp *= -1
    tp = arrow * -1
    for q in range(pos-1, -1, -1):
        if move_check[q]:
            nee[q].rotate(tp)
            tp *= -1

    # for q in nee:
    #     print(q)
    # print()
total = 0
for i in range(4):
    if nee[i][0]:
        total += (2**i)
print(total)
