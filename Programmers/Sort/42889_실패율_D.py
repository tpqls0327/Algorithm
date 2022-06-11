def solution(N, stages):
    length = len(stages)
    dic = {n: 0 for n in range(1, N+1)}
    
    for i in stages:
        if i in dic.keys():
            dic[i] += 1
    arr = []
    for i, j in dic.items():
        try:
            arr.append([(j / length), i])
        except:
            arr.append([0, i])
        length-=j
    arr = sorted(arr, key=(lambda x: (-x[0], x[1])))
    
    return [i[1] for i in arr]

# 더 깔끔한 코드
def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)