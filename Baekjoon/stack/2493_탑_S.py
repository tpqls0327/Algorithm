# 탑
import sys
input = sys.stdin.readline

n = int(input())  
arr = list(map(int, input().split())) 
stack = []
answer = []


for i in range(n):
    while stack:
        print(stack)
        if stack[-1][1] > arr[i]:  
            answer.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:  
        answer.append(0)
    stack.append([i, arr[i]])     # [순서,탑의번호]
    print()

print(" ".join(map(str, answer)))
