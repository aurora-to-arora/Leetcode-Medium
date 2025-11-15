class Solution:
    def myAtoi(self, s: str) -> int:
        MIN = -(2**31)
        MAX = (2**31) - 1
        
        s = s.strip()
        if not s:
            return 0
        
        sign = 1
        i = 0
        n = 0
        
        # sign check
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1
        
        while i < len(s) and s[i].isdigit():
            n = n * 10 + int(s[i])
            i += 1
        
        result = sign * n
        
       
        return max(MIN, min(MAX, result))
