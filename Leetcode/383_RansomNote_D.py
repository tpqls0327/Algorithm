class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        arr_m = [0] * 26
        for i in magazine:
            arr_m[ord(i) - 97] += 1

        for i in ransomNote:
            p = ord(i) - 97
            arr_m[p] -= 1
            if arr_m[p] < 0:
                return False
        return True