class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        n =x
        new_n = 0
        while n:
            rem = n%10
            new_n = new_n*10+rem
            n=n//10
        return new_n==x
        
        
