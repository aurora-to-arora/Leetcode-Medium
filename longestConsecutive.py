class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=set(nums)
        longest = 0
        for n in res:
            if n-1 not in res:
                length = 1
                current = n

                while current+1 in res:
                    current+=1
                    length+=1
                longest= max(longest, length)
        return longest


        
