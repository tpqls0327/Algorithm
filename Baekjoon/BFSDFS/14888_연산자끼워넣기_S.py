# 연산자 끼워 넣기

import itertools
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
operator_num = list(map(int, input().split()))
operator = ['+','-','x','%']

oper = []
for i in range(len(operator_num)):
    if operator_num[i] != 0:
        for _ in range(operator_num[i]):
            oper.append(operator[i])

result = []
for x in itertools.permutations(oper, len(oper)):
    x =list(x) 
    cnt = data[0]
    for i in range(n-1):
        if x[i] == '+':
            cnt = cnt + data[i+1]
        elif x[i] == '-':
            cnt = cnt - data[i+1]
        elif x[i] == 'x':
            cnt = cnt * data[i+1]
        elif x[i] == '%':
            if cnt < 0:
                cnt = -cnt // data[i+1]
                cnt = -cnt    
            else: cnt = cnt // data[i+1]
    result.append(cnt)

print(max(result))
print(min(result))
