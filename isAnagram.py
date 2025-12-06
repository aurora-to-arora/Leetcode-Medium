class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        frq={}

        for ch in s:
            frq[ch]= frq.get(ch,0)+1

        for ch in t:
            if ch not in frq or frq[ch]==0:
                return False
            frq[ch]-=1
        return True        
