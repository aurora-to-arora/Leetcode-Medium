class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX = 2**31 - 1
        MIN = -2**31
        
        # Overflow
        if dividend == MIN and divisor == -1:
            return MAX
        
        # Determine sign
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        
        # Work with absolute values
        n, m = abs(dividend), abs(divisor)
        ans = 0
        
        while n >= m:
            temp = m
            multiple = 1
            while n >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            n -= temp
            ans += multiple
        
        return ans * sign
