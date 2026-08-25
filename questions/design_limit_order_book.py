# Source: WorldQuant
# Question: Design a simple limit order book with add, cancel, and best-price operations.
#

# Order Book Simulation

# You are designing a simple limit order book for a single equity.

# There are three types of operations:
# 	1.	ADD order_id side price quantity
# Add a new order with given id, side (BUY or SELL), price, and quantity.
# 	2.	CANCEL order_id
# Cancel an existing order that hasn’t been filled yet.
# 	3.	BEST
# Print the current best bid and best ask prices (best bid = highest buy price, best ask = lowest sell price).
# If no bids or no asks are present print NONE for that side.

# Orders do not match against each other automatically in this simplified version. You only maintain a book and provide best price responses.

# For each BEST operation print:
# BEST_BID PRICE_QUANTITY BEST_ASK PRICE_QUANTITY
# or BEST_BID PRICE_QUANTITY NONE or NONE BEST_ASK PRICE_QUANTITY depending on state.
from heapq import heappush,heappop

class OrderBook:
    def __init__(self):
        # order_id -> (price, quantity, side)
        self.order_ledger = {}
        # price -> total_quantity
        self.buy_levels = {}
        self.sell_levels = {}
        # heaps for prices
        self.buy_prices = []
        self.sell_prices = []

    def add_order(self, order_id, side, price, quantity):
        if side == "BUY":
            self.buy_levels[price] = self.buy_levels.get(price, 0) + quantity
            heappush(self.buy_prices, -price)
        else:
            self.sell_levels[price] = self.sell_levels.get(price, 0) + quantity
            heappush(self.sell_prices, price)
        self.order_ledger[order_id] = (price, quantity, side)

    def cancel_order(self, order_id):
        if order_id in self.order_ledger:
            price, quantity, side = self.order_ledger.pop(order_id)
            if side == "BUY":
                self.buy_levels[price] -= quantity
                if self.buy_levels[price] == 0:
                    del self.buy_levels[price]
            else:
                self.sell_levels[price] -= quantity
                if self.sell_levels[price] == 0:
                    del self.sell_levels[price]

    def best(self):
        # Clean up buy heap
        while self.buy_prices and -self.buy_prices[0] not in self.buy_levels:
            heappop(self.buy_prices)
        # Clean up sell heap
        while self.sell_prices and self.sell_prices[0] not in self.sell_levels:
            heappop(self.sell_prices)
            
        res = []
        if self.buy_prices:
            best_price = -self.buy_prices[0]
            res.append(f"BEST_BID {best_price} {self.buy_levels[best_price]}")
        else:
            res.append("NONE")
            
        if self.sell_prices:
            best_price = self.sell_prices[0]
            res.append(f"BEST_ASK {best_price} {self.sell_levels[best_price]}")
        else:
            res.append("NONE")
            
        print(" ".join(res))
if __name__ == "__main__":
    order_book = OrderBook()
    order_book.add_order(1, "BUY", 100, 10)
    order_book.add_order(2, "SELL", 101, 10)
    order_book.add_order(3, "BUY", 100, 5) # Same price
    order_book.best() # Should show 100 15
    order_book.cancel_order(1)
    order_book.best() # Should show 100 5