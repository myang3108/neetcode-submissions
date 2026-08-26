class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # choose a single day to buy and choose a diff day to sell
        # each day can be either a buy day. or a sell day
        # return max profit
        # profit = sell - buy

        profit = 0
        currbuy = prices[0]

        for p in prices:
            if p < currbuy:
                currbuy = p
            
            profit = max(profit, p - currbuy)
        
        return profit
