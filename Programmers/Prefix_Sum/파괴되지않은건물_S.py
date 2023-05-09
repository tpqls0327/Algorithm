# 2022 KAKAO BLIND RECUITMENT 파괴되지 않은 건물

# 시간복잡도: 1,000 x 1,000 x 250,000 = 250,000,000,000 (최악의 경우)
# 1억의 연산 : 1초
# 브루트포스 : O(N * M * K) 효율성 테스트케이스에서 시간 초과가 발생
# 누적합 : O(K + N * M)

def prefix_sum(tmp_board, skill):
    # 누적합 2차월 배열 초기화
    prefix_arr = [[0 for j in range(len(tmp_board[0])+1)] for i in range(len(tmp_board)+1)]
    
    # 누적합 배열 생성
    for s in skill:
        t, r1, c1, r2, c2, degree = s  
        if t == 1:    # 타입 비교
            degree = -degree
        prefix_arr[r1][c1] = prefix_arr[r1][c1] + degree  # (x1,y1)에 +n
        prefix_arr[r1][c2+1] = prefix_arr[r1][c2+1] - degree   # (x1,y2+1)에 -n
        prefix_arr[r2+1][c1] = prefix_arr[r2+1][c1] - degree   # (x2+1,y1)에 -n
        prefix_arr[r2+1][c2+1] = prefix_arr[r2+1][c2+1] + degree   # (x2+1,y2+1)에 +n
    
    # 위에서 아래로 누적합
    for i in range(len(prefix_arr)):
        for j in range(len(prefix_arr)-1):
            prefix_arr[j+1][i] += prefix_arr[j][i]
    
    # 왼쪽에서 오른쪽으로 누적합
    for i in range(len(prefix_arr)):
        for j in range(len(prefix_arr)-1):
            prefix_arr[i][j+1] += prefix_arr[i][j]
    
    return prefix_arr
        

def solution(board, skill):
    answer = 0
    prefix_board = prefix_sum(board, skill)
    
    # 누적합 합산
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += prefix_board[i][j]
            # 0보다 큰 정수의 개수 구하기
            if board[i][j] > 0:
                answer += 1
    
    return answer


# 브루트포스 방식 (효율성 통과x)
def calculate_durability(tmp_board, skill):
    for s in skill:
        t, r1, c1, r2, c2, degree = s  
        for i in range(r1,r2+1):
            for j in range(c1, c2+1):
                if t == 1:
                    tmp_board[i][j] = tmp_board[i][j] - degree
                else: tmp_board[i][j] = tmp_board[i][j] + degree       
    return tmp_board 
   
def check_durability(result_board):
    cnt = 0
    for i in range(len(result_board)):
        for j in range(len(result_board[0])):
             if result_board[i][j] > 0:
                cnt += 1
    return cnt

def solution(board, skill):
    answer = 0
    result_board = calculate_durability(board, skill)
    answer = check_durability(result_board)       
    return answer
