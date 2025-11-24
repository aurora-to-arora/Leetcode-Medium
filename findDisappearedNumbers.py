class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = set(nums)
        res=[]
        i=1
        while i<len(nums)+1:
            if i not in n:
                res.append(i)
            i+=1
        return res

        
