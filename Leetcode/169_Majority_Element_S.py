from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_items = Counter(nums)
        max_item = count_items.most_common(n=1)
        return max_item[0][0]
        
