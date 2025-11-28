class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        current = maxx= nums[0]

        for n in nums[1:]:
            current= max(n, current+n)
            maxx= max(maxx, current)
        return maxx

  #OR###############################################
  #dynnamic programming
  class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp=[0]*len(nums)

        for n, val in enumerate(nums):
            dp[n]= max(dp[n-1]+val, val)
        return max(dp)
