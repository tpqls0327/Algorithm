# 7453 합이 0인 네 정수
import sys
input = sys.stdin.readline

# 자리마다 입력 받기
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 두개씩 경우의 수 만들기
ab,cd = [],[]
for i in range(n):
    for j in range(n):
        ab.append(arr[i][0] + arr[j][1])
        cd.append(arr[i][2] + arr[j][3])

ab.sort()
cd.sort()

# 짝 찾기 
i, j = 0, len(cd) - 1 # i는 ab의 시작점, j는 cd의 끝점(투포인터)
ans = 0
while i < len(ab) and j >= 0:
    if ab[i] + cd[j] == 0: 
        nexti, nextj = i + 1, j - 1
        # ab가 같은게 여러개인경우
        while nexti < len(ab) and ab[i] == ab[nexti]: 
            nexti += 1
        # cd가 같은게 여러개인경우
        while nextj >= 0 and cd[j] == cd[nextj]: 
            nextj -= 1
            
        ans += (nexti - i) * (j - nextj) # 핵심코드 -> 중복된 숫자 계산 
        i, j = nexti, nextj

    elif ab[i] + cd[j] > 0: 
        j -= 1
    else:
        i += 1

print(ans)
