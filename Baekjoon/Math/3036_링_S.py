# 링
import math

# 데이터 입력받기
n = int(input())
data = list(map(int, input().split()))

# 기약 분수 구하기   
for i in range(1,n):
    num = math.gcd(data[0],data[i])
    a,b = int(data[0] / num), int(data[i] / num)
    print(a,'/',b, sep='')
