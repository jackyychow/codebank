# Question: Design a voting system with duplicate prevention, cancellation, and top-K queries.
#

import heapq
import unittest
from collections import defaultdict


# Design a Voting System
# Requirements:

# vote(userId, itemId) - User votes for an item. Each user can only vote for an item once (duplicate votes are ignored)
# cancelVote(userId, itemId) - User can cancel their vote for an item
# getItemVotes(itemId) - Returns the total number of votes for a specific item
# getTopKItems(k) - Returns the top K items sorted by vote count (highest votes first) then lexi smallest for tiebreaker

class VotingSystem:
    def __init__(self):
        self.user_votes = defaultdict(set)   # userId -> set of itemIds they've voted
        self.item_count = defaultdict(int)   # itemId -> total votes
        self.vote_frequency=[set()]

    def vote(self, userId, itemId):
        # if user hasn't voted this item yet, count it
        if itemId not in self.user_votes[userId]:
            self.user_votes[userId].add(itemId)
            self.vote_frequency[self.item_count[itemId]].add(itemId)
            self.vote_frequency[self.item_count[itemId]].remove(itemId)
            self.item_count[itemId] += 1
            if self.item_count[itemId]>=len(self.vote_frequency)-1:
                self.vote_frequency.append(set())
            self.vote_frequency[self.item_count[itemId]].add(itemId)
            

    def cancelVote(self, userId, itemId):
        # if user had voted this item, remove it
        if itemId in self.user_votes[userId]:
            self.user_votes[userId].remove(itemId)
            self.vote_frequency[self.item_count[itemId]].remove(itemId)
            self.item_count[itemId] -= 1
            self.vote_frequency[self.item_count[itemId]].add(itemId)

            # optional cleanup if count hits 0

    def getItemVotes(self, itemId):
        return self.item_count[itemId]

    def getTopKItems(self, k):
        result=[]
        print(self.vote_frequency)

        for i in range(len(self.vote_frequency)-1,0,-1):
            if len(result)==k:
                break
            if len(self.vote_frequency[i])>0 and len(self.vote_frequency[i])<=k-len(result):
                result+=[x for x in self.vote_frequency[i]]
            else:
                curr_list=[x for x in self.vote_frequency[i]]
                curr_list.sort()
                result+=curr_list[:k-len(result)]
            

        return result


        #Too inefficient nlogn
        # return list of itemIds with highest counts
        # build a heap of (-count, itemId) or use nlargest
        # We'll do nlargest over all items
        # tie-break rule: higher count first, then lexicographically smaller itemId
        # heap_input = [(-cnt, itemId) for itemId, cnt in self.item_count.items()]
        # result = []

        # if k>=len(heap_input):
        #     heap_input.sort()
        #     return [x[1] for x in heap_input]

        # heapq.heapify(heap_input)
        # for _ in range(min(k, len(heap_input))):
        #     neg_cnt, itemId = heapq.heappop(heap_input)
        #     result.append(itemId)
        # return result

class TestVotingSystem(unittest.TestCase):

    def setUp(self):
        """Initialize a fresh VotingSystem for each test"""
        self.vs = VotingSystem()

    # Basic vote functionality
    def test_single_vote(self):
        """Test basic voting"""
        self.vs.vote(1, 10)
        self.assertEqual(self.vs.getItemVotes(10), 1)

    def test_multiple_votes_same_item(self):
        """Test multiple users voting for same item"""
        self.vs.vote(1, 10)
        self.vs.vote(2, 10)
        self.vs.vote(3, 10)
        self.assertEqual(self.vs.getItemVotes(10), 3)

    def test_user_votes_multiple_items(self):
        """Test one user voting for multiple items"""
        self.vs.vote(1, 10)
        self.vs.vote(1, 20)
        self.vs.vote(1, 30)
        self.assertEqual(self.vs.getItemVotes(10), 1)
        self.assertEqual(self.vs.getItemVotes(20), 1)
        self.assertEqual(self.vs.getItemVotes(30), 1)

    # Duplicate vote prevention
    def test_duplicate_vote_ignored(self):
        """Test that duplicate votes from same user are ignored"""
        self.vs.vote(1, 10)
        self.vs.vote(1, 10)  # Same user, same item
        self.assertEqual(self.vs.getItemVotes(10), 1)

    def test_duplicate_vote_multiple_times(self):
        """Test multiple duplicate votes are all ignored"""
        self.vs.vote(1, 10)
        self.vs.vote(1, 10)
        self.vs.vote(1, 10)
        self.vs.vote(1, 10)
        self.assertEqual(self.vs.getItemVotes(10), 1)

    # Cancel vote functionality
    def test_cancel_vote(self):
        """Test canceling a vote"""
        self.vs.vote(1, 10)
        self.assertEqual(self.vs.getItemVotes(10), 1)
        self.vs.cancelVote(1, 10)
        self.assertEqual(self.vs.getItemVotes(10), 0)

    def test_cancel_nonexistent_vote(self):
        """Test canceling a vote that wasn't cast doesn't cause errors"""
        self.vs.cancelVote(1, 10)  # Should not raise error
        self.assertEqual(self.vs.getItemVotes(10), 0)

    def test_cancel_then_revote(self):
        """Test user can vote again after canceling"""
        self.vs.vote(1, 10)
        self.vs.cancelVote(1, 10)
        self.vs.vote(1, 10)
        self.assertEqual(self.vs.getItemVotes(10), 1)

    def test_cancel_one_of_many_votes(self):
        """Test canceling one vote while others remain"""
        self.vs.vote(1, 10)
        self.vs.vote(2, 10)
        self.vs.vote(3, 10)
        self.vs.cancelVote(2, 10)
        self.assertEqual(self.vs.getItemVotes(10), 2)

    # Top K functionality
    def test_top_k_single_item(self):
        """Test getting top 1 item"""
        self.vs.vote(1, 10)
        self.vs.vote(2, 10)
        result = self.vs.getTopKItems(1)
        self.assertEqual(result, [10])

    def test_top_k_multiple_items(self):
        """Test getting top K items sorted by vote count"""
        self.vs.vote(1, 10)
        self.vs.vote(2, 10)
        self.vs.vote(3, 10)

        self.vs.vote(1, 20)
        self.vs.vote(2, 20)

        self.vs.vote(1, 30)

        result = self.vs.getTopKItems(3)
        self.assertEqual(result, [10, 20, 30])

    def test_top_k_with_ties_lexicographic_ordering(self):
        """Test items with same vote count are ordered lexicographically"""
        self.vs.vote(1, 5)
        self.vs.vote(1, 3)
        self.vs.vote(1, 7)
        # All have 1 vote each, should be ordered: 3, 5, 7
        result = self.vs.getTopKItems(3)
        self.assertEqual(result, [3, 5, 7])

    def test_top_k_greater_than_items(self):
        """Test requesting K greater than number of items"""
        self.vs.vote(1, 10)
        self.vs.vote(2, 20)
        result = self.vs.getTopKItems(5)
        self.assertEqual(len(result), 2)
        self.assertIn(10, result)
        self.assertIn(20, result)

    def test_top_k_empty_system(self):
        """Test getting top K from empty voting system"""
        result = self.vs.getTopKItems(5)
        self.assertEqual(result, [])

    def test_top_k_k_equals_zero(self):
        """Test getting top 0 items"""
        self.vs.vote(1, 10)
        result = self.vs.getTopKItems(0)
        self.assertEqual(result, [])

    def test_top_k_partial_bucket_extraction(self):
        """Test extracting only some items from a bucket (forces else branch)"""
        # Create a bucket with 5 items all having the same vote count
        self.vs.vote(1, 9)
        self.vs.vote(1, 5)
        self.vs.vote(1, 3)
        self.vs.vote(1, 7)
        self.vs.vote(1, 1)
        # All 5 items have 1 vote each

        # Now ask for top 2 items
        # Should get [1, 3] (first 2 lexicographically from the bucket of 5)
        result = self.vs.getTopKItems(2)
        self.assertEqual(result, [1, 3])

    # Integration tests
    def test_complex_scenario(self):
        """Test a complex scenario with multiple operations"""
        # Vote phase
        self.vs.vote(1, 100)
        self.vs.vote(2, 100)
        self.vs.vote(3, 100)

        self.vs.vote(1, 200)
        self.vs.vote(2, 200)

        self.vs.vote(1, 300)

        # Check individual votes
        self.assertEqual(self.vs.getItemVotes(100), 3)
        self.assertEqual(self.vs.getItemVotes(200), 2)
        self.assertEqual(self.vs.getItemVotes(300), 1)

        # Check top K
        top_2 = self.vs.getTopKItems(2)
        self.assertEqual(top_2[0], 100)
        self.assertEqual(top_2[1], 200)

        # Cancel a vote
        self.vs.cancelVote(3, 100)
        self.assertEqual(self.vs.getItemVotes(100), 2)

        # Top K should now have 100 and 200 tied at 2 votes
        top_2 = self.vs.getTopKItems(2)
        self.assertEqual(len(top_2), 2)
        self.assertIn(100, top_2)
        self.assertIn(200, top_2)


if __name__ == "__main__":
    unittest.main()
    vs=VotingSystem()
    vs.vote(1, 10)
    vs.vote(2, 10)
    result = vs.getTopKItems(1)
    print(result)