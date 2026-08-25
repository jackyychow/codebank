# Question: Design a rate limiter with a request limit and time window.
#

from collections import deque, defaultdict

class RateLimiter:
    def __init__(self, max_requests, window_seconds):
        self.max_requests = max_requests
        self.window = window_seconds
        # map clientId -> deque of timestamps (ints)
        # if only one client, just use a single deque
        self.requests = defaultdict(deque)

    def allowRequest(self, timestamp, clientId):
        q = self.requests[clientId]

        # evict old timestamps that are now outside the window
        cutoff = timestamp - self.window
        while q and q[0] <= cutoff:
            q.popleft()

        if len(q) < self.max_requests:
            q.append(timestamp)
            return True
        else:
            return False