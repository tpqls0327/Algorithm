# 숫자의 개수

n1 = int(input())
n2 = int(input())
n3 = int(input())
data = n1 * n2 * n3

result = [0 for _ in range(10)]

for d in str(data):
    if d == '0':
        result[0] += 1
    elif d == '1':
        result[1] += 1
    elif d == '2':
        result[2] += 1
    elif d == '3':
        result[3] += 1
    elif d == '4':
        result[4] += 1
    elif d == '5':
        result[5] += 1
    elif d == '6':
        result[6] += 1
    elif d == '7':
        result[7] += 1
    elif d == '8':
        result[8] += 1
    elif d == '9':
        result[9] += 1

for i in result:
    print(i)
    
    
