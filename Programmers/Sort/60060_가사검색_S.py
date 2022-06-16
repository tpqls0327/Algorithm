# 가사검색 

from bisect import bisect_left, bisect_right

data = [[] for _ in range(10001)]
reversed_data = [[] for _ in range(10001)]
    
def count_by_range(data, left_value, right_value):
    right_index = bisect_right(data, right_value)
    left_index = bisect_right(data, left_value)
    return right_index - left_index
    
def solution(words, queries):
    answer = []

    for word in words:
        data[len(word)].append(word)
        reversed_data[len(word)].append(word[::-1])

    for i in range(10001):
        data[i].sort()
        reversed_data[i].sort()

    for q in queries:
        if q[0] == '?':    # 접두어가 '?'
            result = count_by_range(reversed_data[len(q)], q[::-1].replace('?','a'), q[::-1].replace('?','z'))
        else:
            result = count_by_range(data[len(q)], q.replace('?','a'), q.replace('?','z'))
        answer.append(result)
    return answer
