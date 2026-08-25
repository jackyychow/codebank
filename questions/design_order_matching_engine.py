# Source: WorldQuant
# Question: Design an order-matching engine with price-time priority.
#

from sys import stdin
from collections import defaultdict, deque
import heapq

BUY, SELL = "BUY", "SELL"

class Order:
    def __init__(self, oid: str, side: str, price: int, qty: int):
        self.id = oid
        self.type = side  # BUY / SELL
        self.price = price
        self.qty = qty
        self.active = True

class Engine:
    def __init__(self):
        # price -> deque(order_ids), FIFO within price
        self.buy_book  = defaultdict(deque)
        self.sell_book = defaultdict(deque)
        # heaps for best prices (lazy deletion of price levels)
        self.buy_heap, self.sell_heap = [], []  # buy uses -price (max-heap), sell uses +price (min-heap)
        # id -> Order
        self.order_book = {}

    def _get_book(self, side):  # BUY/SELL -> book
        return self.buy_book if side == BUY else self.sell_book

    def _get_heap(self, side):  # BUY/SELL -> heap
        return self.buy_heap if side == BUY else self.sell_heap

    def _heappush_price(self, side, price):
        if side == BUY:
            heapq.heappush(self.buy_heap, -price)   # store negative for max-heap
        else:
            heapq.heappush(self.sell_heap, price)

    def _get_best_price(self, side):
        book = self._get_book(side)
        heap = self._get_heap(side)
        while heap:
            p = -heap[0] if side == BUY else heap[0]
            q = book.get(p)
            if q:
                while q and (
                    q[0] not in self.order_book or
                    not self.order_book[q[0]].active or
                    self.order_book[q[0]].qty == 0 or
                    self.order_book[q[0]].type != side or     # NEW: side check
                    self.order_book[q[0]].price != p          # NEW: price check
                ):
                    q.popleft()
                if q:
                    return p
                del book[p]
            heapq.heappop(heap)
        return None

    def _can_match(self, incoming_side, incoming_price):
        if incoming_side == BUY:
            best_ask = self._get_best_price(SELL)
            return best_ask is not None and incoming_price >= best_ask, best_ask
        else:
            best_bid = self._get_best_price(BUY)
            return best_bid is not None and incoming_price <= best_bid, best_bid

    # ---- API ----
    def new_order(self, is_buy: bool, price: int, quantity: int, oid: str):
        side = BUY if is_buy else SELL
        order = Order(oid, side, price, quantity)
        self.order_book[oid] = order

        # match against opposite side while crossing
        while order.qty > 0:
            can, best_price = self._can_match(order.type, order.price)
            if not can:
                break
            opp_side = SELL if order.type == BUY else BUY
            opp_book = self._get_book(opp_side)
            q = opp_book.get(best_price)
            if not q:
                break  # should be rare due to cleaning; loop will try again after heap pops

            
            # after you computed best_price and got current_queue = book[best_price]
            top_id = q[0]
            old = self.order_book.get(top_id)
            if (not old or not old.active or old.qty == 0 or
                old.type != side or old.price != best_price):   # NEW: guard
                q.popleft()
                continue
            

            traded = min(order.qty, old.qty)
            # trade at resting (old) order's price
            print(f"TRADE {order.id} {old.id} {old.price} {traded}")

            order.qty -= traded
            old.qty   -= traded
            if old.qty == 0:
                old.active = False
                q.popleft()  # remove fully filled resting order

        if order.qty > 0:
            self._get_book(order.type)[order.price].append(order.id)
            self._heappush_price(order.type, order.price)
            print(f"INSERT {order.type} {order.id} {order.price} {order.qty}")
        else:
            # fully filled: remove from map so later CANCEL/MODIFY on same id are ignored
            del self.order_book[order.id]

    def cancel(self, oid: str):
        o = self.order_book.get(oid)
        if not o or not o.active:
            return
        print(f"CANCEL {oid} {o.qty}")
        o.active = False
        o.qty = 0  # lazy removal from book

    def modify(self, oid: str, is_buy: bool, price: int, quantity: int):
        o = self.order_book.get(oid)
        if not o or not o.active:
            return
        # loses time priority even if fields unchanged
        print(f"CANCEL {oid} {o.qty}")
        o.active = False
        o.qty = 0
        self.new_order(is_buy, price, quantity, oid)


# ---- driver ----
if __name__ == "__main__":
    engine = Engine()
    for line in stdin:
        if not line.strip():
            continue
        t = line.split()
        if t[0] in (BUY, SELL):
            engine.new_order(t[0] == BUY, int(t[1]), int(t[2]), t[3])
        elif t[0] == "CANCEL":
            engine.cancel(t[1])
        elif t[0] == "MODIFY":
            engine.modify(t[1], t[2] == BUY, int(t[3]), int(t[4]))
