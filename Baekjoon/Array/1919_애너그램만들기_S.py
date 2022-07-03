# 애너그램 만들기

num1 = input()
num2 = input()

a = [0]*26
b = a[:]
ans = 0

for i in num1:
    a[ord(i)-97] += 1
for i in num2:
    b[ord(i)-97] += 1

for i in range(26):
    ans += abs(a[i]-b[i])
    
print(ans)
