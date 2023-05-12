# 2022 KAKAO BLIND RECRUITMENT k진수에서 소수 개수 구하기



# 10진수 -> k진수 변환
def transformate_decimal(n, k):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력
    return rev_base[::-1]

# 소수 판별
def is_prime_number(n):
    # 2부터 x의 제곱근까지의 모든 수를 확인 ex) [1,2,4,8,16] : 가운데 수를 기준으로 대칭적으로 곱을 통해 16을 만들 수 있음
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 조선에 맞는 소수 찾기
def find_primeNum(data):
    cnt = 0   # 소수 개수
    num = ''  # 소수 판별할 수
    idx = 0   # 인덱스 번호
    
    while True:
        if idx == len(data):
            break
        # 오른쪽으로 idx를 이동하면서 0을 만날때마다 비교
        if data[idx] != '0':
            num += str(data[idx])
        else:
            if num != '':
                print(num)
                if num != '1' and is_prime_number(int(num)):    # 소수판별
                    cnt += 1
                num = ''                
        idx += 1
        
    # 마지막 계산
    if num != "":
        if num != '1' and is_prime_number(int(num)):    # 소수판별
            cnt += 1
    return cnt


def solution(n, k):
    data = transformate_decimal(n,k)    # 진수 변환
    answer = find_primeNum(data)     # 조선에 맞는 소수 찾기
    return answer
