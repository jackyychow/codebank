# Question: Find the minimum number of carpark lots required for overlapping arrivals and departures.
#

import unittest


def min_carpark(arrival,departure):
    arr=[]

    for i in range(len(arrival)):
        arr.append((arrival[i],1))
        arr.append((departure[i],-1))
    
    arr.sort(key=lambda x:(x[0],x[1]))
    max_lots=0
    occupied=0
    for _, ele in arr:
        occupied+=ele
        max_lots=max(max_lots,occupied)
    
    return max_lots


class CarparkTest(unittest.TestCase):
    def test_happy(self):
        arrival=[1,4,10]
        departure=[5,6,12]
        self.assertEqual(min_carpark(arrival,departure),2)
    
    def test_simultaneous_arrival_departure(self):
        # Car 1: arrives at 1, leaves at 2
        # Car 2: arrives at 2, leaves at 3
        # At time 2: Car 1 leaves AND Car 2 arrives (should need only 1 lot)
        arrival=[1,2]
        departure=[2,3]
        self.assertEqual(min_carpark(arrival,departure),1)
    
    def test_multiple_simultaneous_events(self):
        # Multiple cars arriving and leaving at same time
        arrival=[1,1,3,3]
        departure=[2,3,4,4]
        self.assertEqual(min_carpark(arrival,departure),2)
    
    def test_single_car(self):
        arrival=[5]
        departure=[10]
        self.assertEqual(min_carpark(arrival,departure),1)
    
    def test_no_overlap(self):
        # Cars arrive after previous ones leave
        arrival=[1,3,5]
        departure=[2,4,6]
        self.assertEqual(min_carpark(arrival,departure),1)
    
    def test_all_same_time_arrival_departure(self):
        # All cars arrive at time 1 and leave at time 2
        arrival=[1,1,1]
        departure=[2,2,2]
        self.assertEqual(min_carpark(arrival,departure),3)
if __name__=="__main__":
    unittest.main(verbosity=2)