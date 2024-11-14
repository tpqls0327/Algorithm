class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        single_num = set()
        duple_num = set()

        for num in nums:
            if num in single_num:
                duple_num.add(num)
            else: single_num.add(num)

        ans = 0
        for dn in duple_num:
            ans ^= dn
        return ans
