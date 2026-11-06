class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdct = {}
        tdct = {}

        for i in s:
            sdct[i] = sdct.get(i, 0) + 1
        
        for i in t:
            if i not in sdct:
                return False
            tdct[i] = tdct.get(i, 0) + 1
        
        return sdct == tdct