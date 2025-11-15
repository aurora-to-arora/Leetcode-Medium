class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        # Step 1: Transform
        t = "#" + "#".join(s) + "#"
        n = len(t)
        
        # Array to store radius of palindrome around each index
        p = [0] * n  
        
        center = 0
        right = 0
        
        # Step 2: Manacher
        for i in range(n):
            mirror = 2*center - i   # mirror index of i
            
            if i < right:
                p[i] = min(right - i, p[mirror])
            
            # expand around i
            a = i + (1 + p[i])
            b = i - (1 + p[i])
            
            while a < n and b >= 0 and t[a] == t[b]:
                p[i] += 1
                a += 1
                b -= 1
            
            
            if i + p[i] > right:
                center = i
                right = i + p[i]
        
        max_len = max(p)
        idx = p.index(max_len)
        
        start = (idx - max_len) // 2
        return s[start:start+max_len]
