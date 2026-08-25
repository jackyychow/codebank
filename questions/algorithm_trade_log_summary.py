# Question: Parse a trade log and summarize positions and average buy/sell prices.
#

from collections import defaultdict

class Summary:
    def __init__(self, total_bought, total_sold, net_position, avg_buy_price, avg_sell_price):
        self.total_bought = total_bought
        self.total_sold = total_sold
        self.net_position = net_position
        self.avg_buy_price = avg_buy_price
        self.avg_sell_price = avg_sell_price

    @classmethod
    def empty(cls):
        return cls(0, 0, 0, 0.0, 0.0)   # clean zero-state factory

    def _add_buy_order(self, price: float, quantity: int):
        total_buy_value = self.avg_buy_price * self.total_bought  # recover running total
        self.total_bought += quantity
        self.avg_buy_price = (total_buy_value + price * quantity) / self.total_bought
        self.net_position += quantity

    def _add_sell_order(self, price: float, quantity: int):
        total_sell_value = self.avg_sell_price * self.total_sold
        self.total_sold += quantity
        self.avg_sell_price = (total_sell_value + price * quantity) / self.total_sold
        self.net_position -= quantity

    def to_dict(self) -> dict:
        return {
            "total_bought":    self.total_bought,
            "total_sold":      self.total_sold,
            "net_position":    self.net_position,
            "avg_buy_price":   round(self.avg_buy_price, 2),
            "avg_sell_price":  round(self.avg_sell_price, 2),
        }

def parse_trade_log(log: str) -> dict:
    hm = defaultdict(Summary.empty)            # ✅ factory with no args

    for line in log.strip().splitlines():      # ✅ iterate raw string, skip blank lines
        symbol, side, quantity, price = line.split(":")
        quantity = int(quantity)               # ✅ cast from string
        price = float(price)

        if side == "BUY":
            hm[symbol]._add_buy_order(price, quantity)
        else:
            hm[symbol]._add_sell_order(price, quantity)

    return {symbol: summary.to_dict() for symbol, summary in hm.items()}

