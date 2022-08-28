# 2504 괄호의 값

n = input()
stack = []
cnt = 1
ans = 0
for i in range(len(n)):
  if n[i] == '(':
    cnt *= 2
    stack.append(n[i])
  elif n[i] == '[':
    cnt *= 3
    stack.append(n[i])

  elif n[i] == ')':
    if not stack or stack[-1] == '[':
      ans = 0
      break
    if n[i-1] == '(':
      ans += cnt
    cnt //= 2
    stack.pop() 
  
  else:
    if not stack or stack[-1] == '(':
      ans = 0
      break
    if n[i-1] == '[':
      ans += cnt
    cnt //= 3
    stack.pop()

if stack: ans = 0
print(ans)
