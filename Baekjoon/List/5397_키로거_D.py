import sys
input = sys.stdin.readline

for _ in range(int(input())):
    arr = list(input())
    left, right = [], []

    for c in arr:
        if left and c == "<":
            right.append(left.pop())
        elif right and c == ">":
            left.append(right.pop())
        elif left and c == "-":
            left.pop()
        elif c.isalpha() or c.isalnum():
            left.append(c)

    while right:
        left.append(right.pop())

    print(''.join(left))
