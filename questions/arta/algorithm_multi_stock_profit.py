# Question: Find the best single buy/sell trade across multiple stock timelines.
#
# Return the buy minute, sell minute, ticker, and resulting profit.


class MultiStock:
    # def __init__(self):
    #     self.

    def findMaxProfit(self, stockDict):
        max_profit = 0
        max_ticker = None
        buy_minute = None
        sell_minute = None

        for ticker, timeline in stockDict.items():
            buyTime = 0
            for minute in range(len(timeline)):
                if timeline[minute] - timeline[buyTime] > max_profit:
                    max_profit = timeline[minute] - timeline[buyTime]
                    sell_minute = minute
                    buy_minute = buyTime
                    max_ticker = ticker
                if timeline[minute] < timeline[buyTime]:
                    buyTime = minute
        return (buy_minute, sell_minute, max_ticker, max_profit)


if __name__ == "__main__":
    stock = MultiStock()
    assert stock.findMaxProfit(
        {
            "AAPL": [100, 80, 90, 70, 105],
            "MSFT": [200, 210, 190, 195, 205],
            "TSLA": [50, 55, 60, 45, 48],
        }
    ) == (3, 4, "AAPL", 35)
