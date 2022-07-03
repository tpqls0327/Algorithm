# Strfry

import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    num1, num2 = input().split()
    num1_arr = [0 for _ in range(26)]
    num2_arr = [0 for _ in range(26)]

    for i in num1:
        num1_arr[97 - ord(i)] += 1
    for i in num2:
        num2_arr[97 - ord(i)] += 1

    if num1_arr == num2_arr:
        print('Possible')
    else:
        print('Impossible')
