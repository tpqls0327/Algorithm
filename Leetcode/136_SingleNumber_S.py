'''
XOR 연산을 사용
(A XOR A = 0)이 되는 성질을 활용
모든 수를 XOR하여 마지막에 남는 값을 반환
'''

from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
