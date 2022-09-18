class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        arr = [[sum(row), i] for i, row in enumerate(mat)]
        arr.sort()
        
        return [i for s, i in arr[:k]]