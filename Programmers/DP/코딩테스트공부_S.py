# 프로그래머스 - 코딩 테스트 공부

'''
2차원 동적계획법(DP)

dp[i][j] : 알고력 i, 코딩력 j를 달성하는데 필요한 최소 시간

DP 배열을 정의하면 문제에서 요구하는 답은 dp[목표 알고력][목표 코딩력]
dp[초기 알고력][초기 코딩력] = 0으로 기저 사례를 잡고 나머지 DP 배열의 값은 무한(적당히 큰 값)으로 초기화한 후 for문에서 DP 배열을 업데이트 함

단, dp[alp_max][j]는 알고력이 alp_max " 이상", 코딩력 j를 달성하는데 필요한 최소 시간,
dp[i][cop_max]는 알고력 j, 코딩력 cop_max "이상"을 달성하는데 필요한 최소 시간

시간복잡도: O(목표 알고력 * 목표 코딩력 * (problems 배열의 길이))
'''


def solution(alp, cop, problems):
    INF = 1e9
    max_alp, max_cop = [0, 0]  # 목표값
    
    for problem in problems:
        max_alp = max(max_alp, problem[0])
        max_cop = max(max_cop, problem[1])
    
    dp = [[INF] * (max_cop+1) for _ in range(max_alp+1)]  # 무한값으로 2차원 dp배열 초기화 -> 최소횟수를 갱신해야 하기 때문
   
    # 초기의 알고력(코딩력) 자체가 alp_max(cop_max)보다 높은 경우에 대한 예외처리
    # 이유 : 시작 알고력이 max알고력보다 크거나, 시작 코딩력이 max코딩력보다 클때 dp[alp][cop]=0에서 런타임 에러가 발생
    alp = min(alp, max_alp)  
    cop = min(cop, max_cop)
    
    dp[alp][cop] = 0  # dp[i][j]의 의미 : 알고력 i, 코딩력 j을 도달 할 수 있는 최단시간 (시작점)
    
    for i in range(alp, max_alp+1):
        for j in range(cop, max_cop+1):
            
            # 알고리즘을 공부하여 알고력을 1 높이는 경우
            if i < max_alp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
                
            # 코딩을 공부하여 코딩력을 1 높이는 경우
            if j < max_cop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)
            
            # 문제 하나를 선택하여 알고력과 코딩력을 높이는 경우
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:   # 문제를 풀 수 있는 경우 
                    nxt_alp = min(i+alp_rwd, max_alp)  # 둘중 하나라도 목표값을 넘어가면 안됨
                    nxt_cop = min(j+cop_rwd, max_cop)
                    dp[nxt_alp][nxt_cop] = min(dp[nxt_alp][nxt_cop], dp[i][j] + cost)
             
    return dp[max_alp][max_cop]


    
print(solution(10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]))
