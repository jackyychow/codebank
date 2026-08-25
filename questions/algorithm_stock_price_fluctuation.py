# Question: Implement stock-price updates and current, maximum, and minimum price queries.
#

from heapq import heappop,heappush

class StockPrice:
    def __init__(self):
        self.timestamps = {}
        self.highestTimestamp = 0
        self.minHeap = []
        self.maxHeap = []

    def update(self, timestamp: int, price: int) -> None:
	    #Keep track of current prices
        self.timestamps[timestamp] = price
        self.highestTimestamp = max(self.highestTimestamp, timestamp)
        
		#For maximum/minimum
        heappush(self.minHeap, (price, timestamp))
        heappush(self.maxHeap, (-price, timestamp))

    def current(self) -> int:
	    #Just return the highest timestamp in O(1)
        return self.timestamps[self.highestTimestamp]

    def maximum(self) -> int:
        currPrice, timestamp = heappop(self.maxHeap)
		
		#If the price from the heap doesn't match the price the timestamp indicates, keep popping from the heap
        while -currPrice != self.timestamps[timestamp]:
            currPrice, timestamp = heappop(self.maxHeap)
            
        heappush(self.maxHeap, (currPrice, timestamp))
        return -currPrice

    def minimum(self) -> int:
        currPrice, timestamp = heappop(self.minHeap)
		
		#If the price from the heap doesn't match the price the timestamp indicates, keep popping from the heap
        while currPrice != self.timestamps[timestamp]:
            currPrice, timestamp = heappop(self.minHeap)
            
        heappush(self.minHeap, (currPrice, timestamp))
        return currPrice

###
# Stock Price Fluctuation 
# You are given a stream of records about a particular stock. Each record contains a timestamp and the corresponding price of the stock at that timestamp.

# Unfortunately due to the volatile nature of the stock market, the records do not come in order. Even worse, some records may be incorrect. Another record with the same timestamp may appear later in the stream correcting the price of the previous wrong record.

# Design an algorithm that:

# Updates the price of the stock at a particular timestamp, correcting the price from any previous records at the timestamp.
# Finds the latest price of the stock based on the current records. The latest price is the price at the latest timestamp recorded.
# Finds the maximum price the stock has been based on the current records.
# Finds the minimum price the stock has been based on the current records.
# Implement the StockPrice class:

# StockPrice() Initializes the object with no price records.
# void update(int timestamp, int price) Updates the price of the stock at the given timestamp.
# int current() Returns the latest price of the stock.
# int maximum() Returns the maximum price of the stock.
# int minimum() Returns the minimum price of the stock.
###