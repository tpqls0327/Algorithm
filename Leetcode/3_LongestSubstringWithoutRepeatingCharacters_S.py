# leetcode 3. Longest Substring Without Repeating Characters


from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        q = deque()
        for idx, num in enumerate(s):
            if num in q:
                index = q.index(num)    # 큐 내에 num이 위치하는 index 리턴
                for i in range(index+1):    # 해당 알파벳의 index까지 pop진행
                    q.popleft()    
                q.append(num)
            else:
                q.append(num)
            answer = max(answer, len(q))
            # print(idx, q, answer)
        return answer



'''
case 986) Time Limit Exceeded Error!!

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        for i in range(len(s)):
            num = []
            cnt = 0
            for j in range(i,len(s)):
                if s[j] in num:
                    num = [s[j]]
                    cnt = 1
                else:
                    num.append(s[j])
                    cnt += 1
                answer = max(answer, cnt)
        return answer
'''
