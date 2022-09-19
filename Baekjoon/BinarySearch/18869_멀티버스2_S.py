# 18869 멀티버스 ||
# 좌표 압축 기법

import sys
from collections import defaultdict
input = sys.stdin.readline

m, n = map(int, input().split())
universe = defaultdict(int)
for _ in range(m):
    planets = list(map(int, input().split()))
    keys = sorted(list(set(planets)))
    ranks = {keys[i]: i for i in range(len(keys))}
    add = tuple(ranks[x] for x in planets)
    universe[add] += 1

ans = 0
for cnt in universe.values():
    ans += cnt * (cnt - 1) // 2
print(ans)
