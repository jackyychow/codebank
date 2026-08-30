# Question: Find the minimum number of turns to open a four-wheel lock.
#
# LeetCode 752: Open the Lock.
# 1. what defines a turn? for example if the unlock string is 3000,
# start from 0000 to 3000, is it 1 turn, or 3 turns to get to 3000?
# 2. always 4 digits number in string?
# 3. deadend magnitude
#
#
# ok my idea is to first keep the deadends in a set so at every time to check
# if i am at a deadend, it takes a O(1) lookup to check it. my idea here is to
# use a BFS approach where each queue element is (currCombination, numOfTurns).
# at every turn i popleft from the queue and with the current combination,
# first check if its the unlock, if yes return number of turns (guaranteed smallest).
#  if deadend, dont process. if not, check if it has been visited(keep a visited set).
# if visited, then dont process. else, there are 8 directions we can work with,
# first slot turn up, turn down, second slot turn up, turn down, and so on and so
# forth. does this sit well with you?
#
# Time complexity: O(2N * 10^N)
# Space complexity: O(10^N)


from collections import deque


class CombinationLock:
    def findMinTurns(self, target, deadends):
        deadSet = set(deadends)
        if "0000" in deadSet or target in deadSet:
            return -1

        q = deque([("0000", 0)])
        visited = {"0000"}

        while q:
            currLock, currTurn = q.popleft()
            if currLock == target:
                return currTurn
            if currLock in deadSet:
                continue
            for slot in range(len(currLock)):
                for movement in (1, -1):
                    temp = (int(currLock[slot]) + movement + 10) % 10
                    nextLock = currLock[:slot] + str(temp) + currLock[slot + 1 :]
                    if nextLock not in visited:
                        visited.add(nextLock)
                        q.append((nextLock, currTurn + 1))

        return -1

    def findMinTurns_bidirectional(self, target, deadends):
        dead = set(deadends)
        if "0000" in dead or target in dead:
            return -1
        if target == "0000":
            return 0

        front, back = {"0000"}, {target}
        visited = set(deadends)
        turns = 0

        while front and back:
            # Always expand the smaller frontier to save memory
            if len(front) > len(back):
                front, back = back, front

            next_front = set()
            for curr in front:
                # The two search ripples intersected!
                if curr in back:
                    return turns
                visited.add(curr)

                for i in range(4):
                    for move in (1, -1):
                        nxt = curr[:i] + str((int(curr[i]) + move + 10) % 10) + curr[i + 1:]
                        if nxt not in visited:
                            next_front.add(nxt)

            front = next_front
            turns += 1

        return -1

if __name__ == "__main__":
    lock = CombinationLock()
    assert lock.findMinTurns("0009", []) == 1
    assert lock.findMinTurns("0202", ["0201", "0101", "0102", "1212", "2002"]) == 6
    assert lock.findMinTurns("0000", ["0000"]) == -1
    assert lock.findMinTurns_bidirectional("0009", []) == 1
