# leetcode 5) Longest Palindromic Substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check_palindrome(start, end):
            end = end - 1
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        answer = ""
        for i in range(len(s), 0, -1):
            for j in range(0,len(s)-i+1):
                if check_palindrome(j,j+i):
                    return s[j:j+i]      

'''
testcase 69) Time Limit Exceeded Eroor!!

def check_palindromic(s):
    mid = len(s) // 2 
    if len(s) % 2 == 0:    # 짝수
        reversed_s = reversed(list(s[mid:]))
        reversed_s = ''.join(reversed_s)
        if s[0:mid] == reversed_s:
            return True
    else:    # 홀수
        reversed_s = reversed(list(s[mid+1:]))
        reversed_s = ''.join(reversed_s)
        if s[0:mid] == reversed_s:
            return True
    return False

class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ""
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if check_palindromic(s[i:j]):
                    if len(s[i:j]) > len(answer): answer = s[i:j]
        return answer
'''
