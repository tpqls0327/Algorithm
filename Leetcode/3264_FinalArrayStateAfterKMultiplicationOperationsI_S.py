class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            min_idx = nums.index(min(nums))
            nums[min_idx] *= multiplier
        return nums
