class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        money=0
        stock=-prices[0]
        
        for price in prices:
            old_money=money

            stock=max(stock,old_money-price)
            money=max(money,stock+price-fee)

        return money    