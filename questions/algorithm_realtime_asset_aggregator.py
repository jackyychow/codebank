# Question: Maintain the top three traded assets over a rolling five-second window.
#
# Timestamps must be supplied in nondecreasing order.

import unittest
import heapq
from collections import defaultdict, deque


class RealTimeAssetAggregator:
    def __init__(self):
        self.trade = defaultdict(int)
        self.stream = deque()

    def add_trade(self, timestamp, ticker, volume):
        while self.stream and timestamp - self.stream[0][0] > 5:
            _, old_ticker, old_volume = self.stream.popleft()
            remaining = self.trade[old_ticker] - old_volume
            if remaining:
                self.trade[old_ticker] = remaining
            else:
                del self.trade[old_ticker]
        self.stream.append((timestamp, ticker, volume))
        self.trade[ticker] += volume

    def get_top_3(self):
        return heapq.nlargest(3, self.trade.items(), key=lambda x: x[1])


class TestRealTimeAssetAggregator(unittest.TestCase):
    def test_accumulates_trades_per_ticker(self):
        agg = RealTimeAssetAggregator()

        agg.add_trade(100, "AAPL", 10)
        agg.add_trade(101, "AAPL", 5)
        agg.add_trade(102, "MSFT", 20)

        self.assertEqual(
            agg.get_top_3(),
            [("MSFT", 20), ("AAPL", 15)],
        )

    def test_trade_at_exactly_five_seconds_is_kept(self):
        agg = RealTimeAssetAggregator()

        agg.add_trade(0, "AAPL", 10)
        agg.add_trade(5, "MSFT", 20)

        self.assertEqual(
            agg.get_top_3(),
            [("MSFT", 20), ("AAPL", 10)],
        )

    def test_only_expired_events_are_removed(self):
        agg = RealTimeAssetAggregator()

        agg.add_trade(0, "AAPL", 10)
        agg.add_trade(4, "AAPL", 7)
        agg.add_trade(6, "MSFT", 1)

        self.assertEqual(
            agg.get_top_3(),
            [("AAPL", 7), ("MSFT", 1)],
        )

    def test_returns_top_three_tickers(self):
        agg = RealTimeAssetAggregator()

        for ticker, volume in [
            ("A", 5),
            ("B", 20),
            ("C", 10),
            ("D", 15),
        ]:
            agg.add_trade(1, ticker, volume)

        self.assertEqual(
            agg.get_top_3(),
            [("B", 20), ("D", 15), ("C", 10)],
        )

    def test_expired_tickers_are_not_returned(self):
        agg = RealTimeAssetAggregator()

        agg.add_trade(0, "AAPL", 10)
        agg.add_trade(6, "MSFT", 20)

        self.assertEqual(agg.get_top_3(), [("MSFT", 20)])


if __name__ == "__main__":
    unittest.main()
