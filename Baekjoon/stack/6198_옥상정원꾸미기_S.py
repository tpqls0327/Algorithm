# 옥상 정원 꾸미기

import sys
input = sys.stdin.readline

# 빌딩의 개수 및 높이
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

# 각 빌딩들이 바라볼 수 있는 빌딩의 개수
result = 0

# 빌딩의 높이
stack = []

# 모든 빌딩 탐색
for i in range(n):
    # Stack에 빌딩의 정보가 존재한다면
    while stack:
        # 현재 탐색하고 있는 빌딩의 높이가 Stack top보다 크거나 같다면
        if (arr[i] >= stack[-1]):
            # 현재 탐색하고 있는 빌딩의 높이가 top보다 작아질때까지 Stack top 제거
            stack.pop()
        # 현재 탐색하고 있는 빌딩의 높이가 Stack top보다 작다면
        else:
            # Stack에 존재하는 빌딩 수
            result += len(stack)
            break
    # 현재 탐색하고 있는 빌딩의 정보를 Stack에 삽입 (빌딩의 높이)
    stack.append(arr[i])

print(result)
