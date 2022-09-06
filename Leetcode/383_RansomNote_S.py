class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map = [0]*26
        for i in ransomNote:
            map[ord(i)-ord('a')] +=1
        
        for i in magazine:
            if map[ord(i)-ord('a')] > 0:
                map[ord(i)-ord('a')] -= 1
        return sum(map) == 0
