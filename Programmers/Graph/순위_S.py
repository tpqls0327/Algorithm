# 순위_S.py 20230313

def solution(n, results):
    INF = int(1e9)
    
    # 노드의 개수, 간선의 개수 : n
    graph = [[INF] * (n+1) for _ in range(n+1)]
    
    # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a == b:
                graph[a][b] = 0
    
    # 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
    for result in results:
        a,b = result[0], result[1]
        graph[a][b] = 1
    
    # 점화식에 따라 플로이드 워셜 알고리즘을 수행
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    
    # 수행한 결과를 출력
    result = 0
    for i in range(1, n+1):
        cnt = 0
        for j in range(1, n+1):
            if graph[i][j] != INF or graph[j][i] != INF:
                cnt += 1
        if cnt == n:
            result += 1
            
    return result
