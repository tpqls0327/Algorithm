b_arr = [0 for _ in range(26)]
a_arr = [0 for _ in range(26)]

b = input()
a = input()

for i in b:
    b_arr[ord(i)-97] += 1
for j in a:
    a_arr[ord(j)-97] += 1
cnt = 0

for i in range(26):
    if a_arr[i] != b_arr[i]:
        cnt += (abs(a_arr[i] - b_arr[i]))
print(cnt)