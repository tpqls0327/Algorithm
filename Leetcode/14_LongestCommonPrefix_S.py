class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        1. 가장 길이가 작은 글자의 수(n)만큼 글자 비교
        2. 모든 문자열(str)에서 n의 길이만큼 접두어 비교 
        4. 반복문이 끝날때까지 반환이 안됬다면 "" 반환
        '''
        n = min(strs, key=len)
        size_n = len(n)

        while size_n > 0:
            check_str = n[:size_n]
            cnt = 0
            for str in strs:
                if check_str == str[:size_n]:
                    cnt += 1
            if cnt == len(strs):
                return check_str
            size_n -= 1   
        return ""

