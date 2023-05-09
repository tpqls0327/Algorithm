# 10진수 -> k진수 변환
def transformate_decimal(n, k):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력
    return rev_base[::-1]

# 소수 판별
def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

# 조선에 맞는 소수 찾기
def find_primeNum(data):
    cnt = 0   # 소수 개수
    num = ''  # 소수 판별할 수
    idx = 0   # 인덱스 번호
    print("data:",data)
    
    while True:
        print("idx:", idx)
        print("num", num)
        if idx == len(data):
            break
        # 오른쪽으로 idx를 이동하면서 0을 만날때마다 비교
        if data[idx] == '0':
            if num != '':
                print(num)
                if is_prime_number(int(num)):    # 소수판별
                    cnt += 1
                else:
                    num = ''
        else:
            num += str(data[idx])
            
        idx += 1
        
    return cnt


def solution(n, k):
    answer = -1
    data = transformate_decimal(n,k)
    answer = find_primeNum(data)
    return answer

solution(437674, 3)
