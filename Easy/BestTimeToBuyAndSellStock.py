class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = prices[0]
        maxDiff = 0

        for price in prices:
            # update local minimum
            if price < minPrice:
                minPrice = price

            # the max profit is between this price and a previous local minimum
            if (price - minPrice) > maxDiff:
                maxDiff = (price - minPrice)

        return maxDiff
