"""
122. 买卖股票的最佳时机 II

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        贪心算法, 高频交易，比较前一天和今天的股价，前一天高就前一天卖掉（当天再买），否则今天卖掉，然后今天再买
        时间复杂度：O(n)
        空间复杂度：O(1)
        '''
        if not prices:
            return 0
        buy_price, profit = prices[0], 0
        for i in range(1, len(prices)):
            yesterday, today = prices[i - 1], prices[i]
            profit += max(today, yesterday) - buy_price
            buy_price = today
        return profit
