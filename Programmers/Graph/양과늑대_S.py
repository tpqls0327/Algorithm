# 프로그래머스 - 양과 늑대


def solution(info, edges):
    visited = [0] * len(info)
    answer = []
    
    def dfs(sheep, wolf):
        if sheep > wolf:     # 양의 수가 늑대의 수보다 많은가?
            answer.append(sheep)   # 양의 수를 결과 배열에 저장
        else:   
            return 
        
        for p, c in edges:
            if visited[p] and not visited[c]:     # 부모 노드를 방문한 적이 있는가?
                visited[c] = 1   # 자식 노드 방문처리
                if info[c] == 0:   # 자식 노드를 처음 방문하는가?
                    dfs(sheep+1, wolf)   # 양의 수 업데이트
                else:
                    dfs(sheep, wolf+1)   # 늑대의 수 업데이트
                visited[c] = 0   # 방문처리 되돌리기
    
	# 루트 노드부터 시작
    visited[0] = 1
    dfs(1, 0)

    return max(answer)    # 양의 수를 저장한 배열에서의 최댓값
