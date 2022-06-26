# 못생긴 수

n = int(input())

result = [1]
i = 2
while len(result) < n+2:
    if not i % 2 or not i % 3 or not i % 5:
        if i % 7 == 0:
            i += 1
        else:  
            result.append(i)
            i+=1
    else:
        i+=1
        continue

print(result[-1])
