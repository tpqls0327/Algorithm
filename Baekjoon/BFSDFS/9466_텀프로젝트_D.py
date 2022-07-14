for _ in range(int(input())):
    n = int(input())
    teams = [0] + list(map(int, input().split()))
    visited = [0 for _ in range(n + 1)]
    cnt = 0
    for s in range(1, n+1):
        if not visited[s]:
            start, end = s, s

            while not visited[start]:
                visited[start] = 1
                start = teams[start]

            while end != start:
                cnt += 1
                end = teams[end]

    print(cnt)
