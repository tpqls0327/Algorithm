# 제로

import sys
input = sys.stdin.readline

result = []
for _ in range(int(input())):
    data = int(input())
    if data == 0:
        if len(result) != 0:
            del result[-1]
    else: result.append(data)
print(sum(result))
