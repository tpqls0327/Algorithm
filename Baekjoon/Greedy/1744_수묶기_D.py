n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

if n == 1:
    print(arr[0])
else:
    _sum = 0                # 총 합
    sep = 0                 # 0보다 커지는 인덱스
    if arr[sep] <= 0:       # 0을 찾기 위함
        for k in range(n):
            if arr[k] > 0:  # 0보다 큰 지점이 있다면
                sep = k     # 저장
                break       # 종료
    if arr[-1] <= 0:        # 전체가 음수라면
        sep = n             # 마지막 인덱스

    t1, t2 = arr[:sep], arr[sep:]   # 배열 나누기
    n1, n2 = len(t1), len(t2)       # 두 배열 길이
    if n1 <= 1:             # 길이가 1이하면
        _sum += sum(t1)     # 더하기
    else:                   # 길이가 2 이상
        for i in range(0, n1-1, 2):
            _sum += (t1[i] * t1[i + 1])
        if n1 % 2:          # 홀수라면
            _sum += t1[-1]  # 마지막 숫자 더해주기(가장 작은 것이 보장되므로)
    if n2 <= 1:             # 마찬가지로 양수 배열에서도 진행
        _sum += sum(t2)
    else:
        for i in range(n2-1, 0, -2):
            _sum += (t2[i-1] * t2[i]) if t2[i-1] != 1 else (t2[i-1] + t2[i])
        if n2 % 2:
            _sum += t2[0]

    print(_sum)
