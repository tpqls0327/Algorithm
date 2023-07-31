class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        _max = 0
        for acc in accounts:
            _max = max(_max, sum(acc))
        return _max