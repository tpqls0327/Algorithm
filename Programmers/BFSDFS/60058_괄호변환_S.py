# 괄호변환

def solution(p):
    answer = ''
    if p == '':
        return answer
    
    u, v = balanced(p)
    # '올바른 괄호 문자열'이면 v에 대해 함수를 수행한 결과를 붙여 반환
    if correct(u):
        answer = u + solution(v)
    
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer


# 균형잡힌 괄호 문자열 분할
def balanced(arr):
    left = 0
    right = 0
    for idx, data in enumerate(arr):
        if data == '(':
            left += 1
        else: right += 1
        if left == right:
            return arr[:idx+1], arr[idx+1:]

# 올바른 괄호 문자열 판별
def correct(arr):
    cnt = 0
    for i in arr:
        if i == '(':
            cnt += 1
        else: 
            cnt -= 1
            if cnt < 0:
                return False
    return True
