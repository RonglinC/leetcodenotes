class Solution(object):
    def climbStairs(self, n):
        return self.helper(0,n)

        def helper(i,n):
            if i > n:
                return 0
            if i ==n:
                return 1
            return helper(i+1,n)+helper(i+2,n)

# 一维dp，自底向上
def climbStairs(self, n: int) -> int:
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[-1]



