import sys
n = int(input())
dic = {i: set() for i in range(1, 51)}

for _ in range(n):
    word = sys.stdin.readline().rstrip()
    dic[len(word)].add(word)

for i in range(1, 51):
    if dic[i]:
        print(*sorted(dic[i]), sep='\n')
