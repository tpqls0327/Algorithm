# 실패율

def solution(N, stages):
    cnt = []
    users = len(stages)

    for i in range(1,N+1):
        c = stages.count(i)
        
        if c == 0:                    # 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0으로 정의한다.
            cnt.append((0, i))
        else:
            cnt.append((c/users, i))    # 튜플로 저장
            users -= c
        
    print(cnt)

    result = []
    cnt = sorted(cnt, key=lambda x: -x[0])

    for i in range(len(cnt)):
        result.append(cnt[i][1])
    
    return result
