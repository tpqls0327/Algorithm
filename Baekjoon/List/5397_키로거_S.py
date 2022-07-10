# 키로거

import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    l_list = []
    r_list = []
    data = input()
    
    for i in data:
        if i == '-':
            if len(l_list):
                l_list.pop()
        elif i == '<': 
            if len(l_list):
                r_list.append(l_list.pop())
        elif i == '>':
            if len(r_list):
                l_list.append(r_list.pop())
        else:
            l_list.append(i)
    l_list.extend(reversed(r_list))
    result = ''.join(l_list).strip()
    print(result)
    
