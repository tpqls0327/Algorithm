# 스택 수열

import sys
input = sys.stdin.readline

result = []      # 기호 저장 
stack = []     # 만들어야하는 수열 
tmp_stack = []     # 차례대로 숫자가 들어가는 스택 
n = int(input())
for _ in range(n):
    tmp = int(input())
    stack.append(tmp)

cnt = 1      # 스택에 들어가는 숫자 오름차순 
idx = 0      # stack의 인덱스
while True:
    if idx >= n or cnt > n:     # 핵심 
        break
    if len(tmp_stack) == 0:
        if idx == 0:           # 첫번째 숫자를 넣는 경우
            tmp_stack.append(cnt)
            result.append('+')
        else:                  # 중간에 스택이 모두 pop되어 비어있게되는 경우 
            cnt += 1
            tmp_stack.append(cnt)
            result.append('+')
        continue
    
    if stack[idx] == tmp_stack[-1]:
        tmp_stack.pop()
        idx += 1
        result.append('-')
    else:
        cnt += 1
        tmp_stack.append(cnt)
        result.append('+')

if len(tmp_stack) != 0:
    print('NO')
else:
    for num in result:
        print(num)
