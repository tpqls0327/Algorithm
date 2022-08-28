# 10799 쇠막대기
# 레이져가 나올때 현재 stack[]의 개수만큼 값을 더해줌
# 이전의 값이 ')'였는데 이번에 ')'가 나오면 괄호 하나가 빠지고 하나만 짤리는 거니까 +1

n = input()
ans = 0
stack = []
pre_stack = '#'   # 이전의 값(1을 더할지 스택의 개수만큼 더할지 판별)
for i in n:
    if i == '(':
        stack.append(i)
    else:
        if pre_stack == '(':
            stack.pop()
            ans+=len(stack)
        else:
            stack.pop()
            ans+=1
    pre_stack = i
print(ans)
