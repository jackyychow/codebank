# Source: Akuna
# Question: Determine whether all courses can be completed from prerequisites.
#

# Return true if you can finish all courses. Otherwise, return false.

from collections import defaultdict,deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    # Topological Sort
        prereq=defaultdict(list)
        for post,pre in prerequisites:
            prereq[post].append(pre)

        visited=set()
        cycle=set()
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True

            cycle.add(course)
            for pre in prereq[course]:
                if dfs(pre)==False:
                    return False
            cycle.remove(course)
            visited.add(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True


# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order=[]
        visited=set()
        cycle=set()

        prereq=defaultdict(list)
        for pre,post in prerequisites:
            prereq[post].append(pre)

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True

            cycle.add(course)
            for pre in prereq[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            order.append(course)
            visited.add(course)

            return True




        for course in range(numCourses):
            if not dfs(course):
                return []
        return order[::-1]

# """
# There are n different online courses numbered from 1 to n. You are given an array courses where courses[i] = [durationi, lastDayi] indicate that the ith course should be taken continuously for durationi days and must be finished before or on lastDayi.

# You will start on the 1st day and you cannot take two or more courses simultaneously.

# Return the maximum number of courses that you can take.
# """
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: (x[1], x[0])) # Sorted primarily by last date and secondarily by duration to sequentially iterate over courses.
        history, curr_time = [], 0 # Past is our max heap of durations of courses that we have taken and curr_time is the current time we are at.
        for duration, last_day in courses:
            if curr_time + duration <= last_day: # If we can incorporate this course in our current state then do so.
                heappush(history, -duration) # -ve values stored as Python only has Min Heap available. So to operate it as a Max Heap we store -ve of the values.
                curr_time += duration # Update the curr_time variable.
            else: # Try if replacing longest course with current course can save some time.
                if history: # If HISTORY is not empty
                    longest_course = -history[0] # Longest course done so far.
                    if longest_course > duration: # Check if that course was longer than the current one.
                        heappop(history) # Removing longest_course and adding current course keeps number of courses same but reduces the curr_time.
                        heappush(history, -duration) # Add current course to past.
                        curr_time += duration - longest_course # Update curr_time accordingly
        return len(history)

# """
# You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you should answer whether course uj is a prerequisite of course vj or not.

# Return a boolean array answer, where answer[j] is the answer to the jth query.
# """
class Solution:
    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]],
    ) -> List[bool]:
        adjList = defaultdict(list)
        indegree = [0] * numCourses

        for edge in prerequisites:
            adjList[edge[0]].append(edge[1])
            indegree[edge[1]] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        nodePrerequisites = defaultdict(set)

        while q:
            node = q.popleft()

            for adj in adjList[node]:
                # Add node and prerequisite of the node to the prerequisites of adj
                nodePrerequisites[adj].add(node)
                for prereq in nodePrerequisites[node]:
                    nodePrerequisites[adj].add(prereq)

                indegree[adj] -= 1
                if indegree[adj] == 0:
                    q.append(adj)

        answer = []
        for q in queries:
            answer.append(q[0] in nodePrerequisites[q[1]])

        return answer
