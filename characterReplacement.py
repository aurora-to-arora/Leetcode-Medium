class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frq = {}
        left=0
        max_freq=0
        best =0

        for right, ch in enumerate(s):
            frq[ch]=frq.get(ch,0)+1
            max_freq= max(max_freq, frq[ch])

            while (right-left+1)-max_freq>k:
                frq[s[left]]-=1
                left+=1
            best = max(best, right-left+1)

        return best
        
