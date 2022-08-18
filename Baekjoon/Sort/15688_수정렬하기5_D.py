import sys
arr = [int(sys.stdin.readline()) for _ in range(int(input()))]
print(*sorted(arr))