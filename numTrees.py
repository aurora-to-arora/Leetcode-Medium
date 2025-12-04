#math.comb(2*n,n)//(n+1)

class Solution:
    def numTrees(self, n: int) -> int:

        # dp nums of BST
        # dp[i] += dp[i-j] * dp[j-1] for j in range(0, i+1)
        # dp[0],dp[1] = 1, 1
        # left -> right
        # return dp[n]

        if n <= 0:
            return 0

        dp = [0] * (n+1)
        dp[1], dp[0] = 1, 1
        for i in range(2, n+1):
            for j in range(0, i+1):
                dp[i] += dp[j-1] * dp[i-j]

        return dp[n]
