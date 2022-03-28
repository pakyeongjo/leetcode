class MaxProfit:
    def solution(self, prices):
        max_profit = 0
        min_price = 100001

        for price in prices:
            min_price = price if price < min_price else min_price
            max_profit = max_profit if max_profit > price - min_price else price - min_price

            # min_price = min(min_price, price)
            # max_profit = max(max_profit, price - min_price)

        return max_profit
