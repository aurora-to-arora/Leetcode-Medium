class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0   # pointer to place next non-zero
        
        # Move all non-zero values to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        
        # Fill the remaining spots with zeros
        while j < len(nums):
            nums[j] = 0
            j += 1
