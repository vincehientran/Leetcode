class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        dp = [amount+1 for i in xrange(amount+1)]
        dp[0] = 0
        for i in xrange(1, amount+1):

            for coin in coins:

                if coin <= amount:

                    # pretend "coin" is the last coin needed to make "i"
                    # then the amount of coins needed is
                    # the amount needed to make "i - coin" PLUS 1 coin
                    best = min(dp[i - coin]+1,dp[i])
                    dp[i] = best

        # the answer is the last element in the List
        # if the answer is greater than the "amount"
        # then it is impossible to make the "amount" with the given coin(s)
        if dp[-1] > amount:
            return -1
        else:
            return dp[amount]
