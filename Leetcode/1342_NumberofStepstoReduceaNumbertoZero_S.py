class Solution:
    def numberOfSteps(self, num: int) -> int:
        cnt = 0
        while num:
            num = num-1 if num % 2 else num // 2
            cnt += 1
        return cnt