def Sorting():
    # Quick sort in Python
    def partition(array, low, high): # function to find the partition position
      # choose the rightmost element as pivot
      pivot = array[high]
      # pointer for greater element
      i = low - 1
      # traverse through all elements
      # compare each element with pivot
      for j in range(low, high):
        if array[j] <= pivot:
          # if element smaller than pivot is found
          # swap it with the greater element pointed by i
          i = i + 1
          # swapping element at i with element at j
          (array[i], array[j]) = (array[j], array[i])
      # swap the pivot element with the greater element specified by i
      (array[i + 1], array[high]) = (array[high], array[i + 1])
      # return the position from where partition is done
      return i + 1
    # function to perform quicksort
    def quickSort(array, low, high):
      if low < high:
        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
        # recursive call on the left of pivot
        quickSort(array, low, pi - 1)
        # recursive call on the right of pivot
        quickSort(array, pi + 1, high)

def ArrayManipulation():
    def rotate_array(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        radius=len(matrix)
        for i in range(radius):
            new=[]
            for j in range(radius-1,-1,-1):
                new.append(matrix[j][i])
            matrix.append(new)

        for i in range(radius):
            matrix.pop(0)

        return matrix
        
        # in place rotation
        for i in range(n // 2):
                for j in range((n + 1) // 2):
                    (
                        matrix[i][j],
                        matrix[n - 1 - j][i],
                        matrix[n - 1 - i][n - 1 - j],
                        matrix[j][n - 1 - i],
                    ) = (
                        matrix[n - 1 - j][i],
                        matrix[n - 1 - i][n - 1 - j],
                        matrix[j][n - 1 - i],
                        matrix[i][j],
                    )
    
    def sort_list_of_list(arr: List[List[int]]):
        # Based on index 0 (First index)
        arr=sorted(arr, key=itemgetter(0)) / # arr.sort()
        
    def findQuadruplets(lst, target): 
    # find any 4 in the list that adds to target key
        def valid(val):
            return sum(val) == target
        return list(filter(valid, list(combinations(lst, 4)))) #sol = list(dict.fromkeys(sol)) to remove duplicate entries
    
    def subarraySum(self, nums: List[int], k: int) -> int: # Find number of subarrays adding to target k
        ans, n = 0, len(nums)
        preSum = [nums[0]]
        dic = {}
        dic[0] = 1
        for i in nums[1:]:
            preSum.append(i+preSum[-1])
        for i in preSum:
            if i-k in dic:
                ans+=dic[i-k]
            dic[i] = dic.get(i,0) + 1 
        return ans
########################################################################################################################################################################################################################

def StringManipulation():
    lst=[str(x) for x in lst] #int list to str list
    
    def palindromePartition(x):  
        sol=[]
        length=len(x)
        if (length==0):
            return [[]]
        if (length==1):
            return [[x]]
        for i in range (1,length+1):
            # if isPalindrome(s[:i]):
            y = palindromePartition(x[i:])
            for j in range(len(y)):
                y[j] = [x[:i]]+y[j]
            sol+=y
        return sol
    def reverseString(s:str):
        return s[::-1]
    def allSubStr(s: str):
        return [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
########################################################################################################################################################################################################################
def SlidingWindow():
        dup=set()
        max_len=0
        
        start,end=0,0

        while start<=end and end<len(s):
            if s[end] not in dup:
                max_len=max(max_len,end-start+1)
                dup.add(s[end])
                end+=1
            else:
                while s[start]!=s[end]:
                    dup.remove(s[start])
                    start+=1
                dup.remove(s[end])
                start+=1

        return max_len


########################################################################################################################################################################################################################

def BinarySearch():
    def searchOcurrenceIndex(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        if size==0:
            return [-1,-1]

        # Finding first occurence of element
        start, end = 0, size-1
        while start<=end:
            mid = (start+end)//2
            if nums[mid]>=target:
                end = mid - 1
            else:
                start = mid + 1

        if start<0 or start>=size or not nums[start]==target:
            first=start

        # Finding last occurence of element
        start, end = 0, size-1
        while start<=end:
            mid = (start+end)//2
            if nums[mid]>target:
                end = mid - 1
            elif nums[mid]<target:
                start = mid + 1
            else:
                return mid
        return -1

        start-=1
        if start<0 or start>=size or not nums[start]==target:
            last=start

        return first,last
    
    def binarySearch(self, arr, target):
        l,r=0,len(arr)-1
        while l<r:
            mid=(l+r)//2
            if arr[mid]>=target:
                r=mid
            else:
                l=mid+1
        return arr[l]==target
    
    def lengthOfLongestIncreasingSubsequence(self, nums: List[int]) -> int: #https://leetcode.com/problems/longest-increasing-subsequence/description/
        if len(nums)==0:
            return 0
        l = [nums[0]]
        for num in nums:
            #if num is alredy in the list skip
            if num in l:
                continue
            #if nums is greater than the last element of the list(the max)
            #just append at the end of the list
            if num > l[-1]:
                l.append(num)
            else:
                #binary search of the smallest element of the list
                #that is greater than num
                s, e = 0, len(l)-1
                while e > s:
                    mid = s + (e-s)//2
                    if l[mid] < num:
                        s = mid + 1
                    else:
                        e = mid
                #swap num with the smallest element of the list that is greater than num
                l[e] = num
        return len(l)
########################################################################################################################################################################################################################

def Binary Tree():
    # https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
    def printInorder(root): # 4,2,5,1,6,3,7
        if root:
            printInorder(root.left)
            print(root.val),
            printInorder(root.right)

    def printPostorder(root): # 4,5,2,6,7,3,1
        if root:
            printPostorder(root.left)
            printPostorder(root.right)
            print(root.val),

    def printPreorder(root): # 1,2,4,5,3,6,7
        if root:
            print(root.val),
            printPreorder(root.left)
            printPreorder(root.right)
            
    def maxDepth(root: Optional[TreeNode]) -> int:
          if root == None:
            return 0
          leftDepth = self.maxDepth(root.left)
          rightDepth = self.maxDepth(root.right)
          return  max(leftDepth, rightDepth) + 1
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checkMax(root, mini, maxi) -> bool:
            if root == None:
                return True
            
            if root.val >= maxi or root.val <= mini:
                return False
            
            return checkMax(root.left, mini, root.val) and checkMax(root.right, root.val, maxi)     
            
        if root == None:
            return True
        min_num = -math.inf
        max_num = math.inf
        return checkMax(root, min_num, max_num)
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0,True

            leftDepth, balanced = dfs(node.left)
            leftDepth+=1
            if not balanced:
                return 0,False
            
            rightDepth, balanced = dfs(node.right)
            rightDepth+=1
            if not balanced:
                return 0,False

            if abs(rightDepth-leftDepth)>1:
                return 0,False

            return max(leftDepth,rightDepth),True

        _, balanced=dfs(root)
        return balanced
        OR
        def dfs(node):
            if not node:
                return 0
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            return max(left_height, right_height) + 1
        return dfs(root)!=-1
    
        
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int: #find kth smallest value in BST     
        self.index=0
        self.ans=-1

        def inOrderDFS(node):
            if node:
                inOrderDFS(node.left)
                self.index+=1
                if self.index==k:
                    self.ans=node.val
                inOrderDFS(node.right)
        
        inOrderDFS(root)
        return self.ans
    
    
def BFS():
    def courseSchedule(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int: #https://leetcode.com/problems/shortest-path-in-binary-matrix/
        n = len(grid)
        if grid[0][0] == 1:
            return -1
        path = {}
        start = (0, 0)
        path[start] = 1
        grid[0][0] = 1
        q = deque([(0,0)])
        neighbors = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        while q:
            (i, j) = q.popleft()
            if (i, j) == (n - 1, n - 1):
                break
            for ix, jx in neighbors:
                new_i,new_j=i + ix,j + jx
                if 0 <= new_i and new_i < n and 0 <= new_j and new_j < n and grid[new_i][new_j] == 0:
                    path[(new_i,new_j)] = path[(i, j)] + 1
                    q.append((new_i,new_j))
                    grid[new_i][new_j] = 1 #ensures backtracking
        # print(path)
        if path.get((n - 1, n - 1)):
            return path[(n - 1, n - 1)]
        return - 1
########################################################################################################################################################################################################################

def DynamicProgramming():
    def maxProfit(self, prices: List[int]) -> int:
        # maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
        low=float('inf')
        high=float("-inf")
        profit=0

        for i in range(len(prices)):
            if prices[i]<low:
                low=prices[i]
                high=float("-inf")
            if prices[i]>high:
                high=prices[i]
            if high>low:
                profit=max(profit,high-low)

        return profit
    def rob(self, nums: List[int]) -> int:
        # max profit from the list of int but cannot take adjacent index elements

          if len(nums) <= 2:
            return max(nums)

          sum1 = nums[0]
          sum2 = max(nums[0],nums[1])

          for i in range(2,len(nums)):
            sum1, sum2 = sum2, max(sum2, sum1 + nums[i])
          return max(sum1,sum2)
    
    def findMinArrowShots(self, points: List[List[int]]) -> int:      
        arrows=0
        points.sort()
        print(points)
        
        interval = (float("-inf"), float("-inf"))
        
        for xstart, xend in points:
            if xstart<=interval[1]:
                interval=(max(interval[0],xstart), min(interval[1],xend))
            else:
                arrows+=1
                interval=(xstart,xend)
        return arrows  
      
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:    # Length of longest subsequence of two strings
        # Use 2D DP (https://leetcode.com/problems/longest-common-subsequence/discuss/1832840/Detailed-and-pictured-explanation)
        m = len(text1)
        n = len(text2)
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        print(dp)

        return dp[m][n] 
      
    def solve_knapsack(weights, values, capacity):
      n = len(weights)
      # Initialize a 2D DP table with 0s
      # Rows = items (plus a dummy 0 row)
      # Cols = capacity from 0 to 'capacity'
      dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

      # Build the table bottom-up
      for i in range(1, n + 1):
          current_weight = weights[i-1]
          current_value = values[i-1]

          for w in range(capacity + 1):
              if current_weight <= w:
                  # Max of (don't take, do take)
                  dp[i][w] = max(dp[i-1][w], 
                                 current_value + dp[i-1][w - current_weight])
              else:
                  # Item is too heavy, carry over the previous best
                  dp[i][w] = dp[i-1][w]

      return dp[n][capacity]
########################################################################################################################################################################################################################

def LinkedList():
    def reverseLL(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        # DFS
        def dfs(node):
            if not node.next:
                return node,node
            
            prev,head=dfs(node.next)
            prev.next=node
            return node,head     
        prev,head=dfs(head)
        prev.next=None
        return head
        
        # BFS
        q=deque()
        while head:
            q.append(head)
            head=head.next        
        head=q.pop()
        prev=head
        while q:
            prev.next=q.pop()
            prev=prev.next  
        prev.next=None
        return head
    
    def hasCycle(self, head: Optional[ListNode]) -> bool: # Check cycle exist in LL
#         Floyd Cycle
        if not head:
            return False
        slow=head
        fast=head.next
        
        while fast!=slow:
            if not fast or not fast.next:
                return False
            slow=slow.next
            fast=fast.next.next
        return True
    
def Graph():
    def cloneGraph(self, node: 'Node') -> 'Node': #https://leetcode.com/problems/clone-graph/
        if not node: 
            return node

        q = deque([node])
        clones = {node.val: Node(node.val, [])}

        while q:
            curr = q.popleft()
            curr_clone = clones[curr.val]

            for nbr in curr.neighbors:
                if nbr.val not in clones:
                    clones[nbr.val] = Node(nbr.val, [])
                    q.append(nbr)

                curr_clone.neighbors.append(clones[nbr.val])

        return clones[node.val]
########################################################################################################################################################################################################################

def Stack():
    def sumSubarrayMins(self, arr: List[int]) -> int: #Find total sum of all subarray minimums, https://leetcode.com/problems/sum-of-subarray-minimums/
        ##Monotonic Stack approach
        stack=[-1]##idx
        ans=0
        arr.append(-inf)
        for i,n in enumerate(arr):
            while len(stack)>1 and n<=arr[stack[-1]]:##len(stack>1 because -1 is imaginary idx and there won't be any number at -1 idx)
                curr=stack.pop()
                ans+=arr[curr]*(curr-stack[-1])*(i-curr)
            stack.append(i)
            ans%=10**9+7
        return ans

########################################################################################################################################################################################################################

def Interval():
     def insertInterval(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]: # Insert 1 invertal and merge intervals    
        if len(intervals)==0:
            return [newInterval]
        q=deque(intervals)
        res=[]    
        while q:
            l,r=q[0]
            if newInterval[1]<l:
                break
            elif r<newInterval[0]:
                res.append([l,r])
                q.popleft()
            else:
                newInterval=[min(l,newInterval[0]),max(r,newInterval[1])]
                q.popleft()        
        res.append(newInterval)
        while q:
            res.append(q.popleft())    
        return res
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]: #Merge intervals
        intervals.sort()
        q=deque(intervals[1:])
        res=[]
        
        start,end=intervals[0]
        while q:
            curr=q.popleft()
            if end<curr[0]:
                res.append([start,end])
                start,end=curr
            else: 
                start=min(start,curr[0])
                end=max(end,curr[1])
                
        res.append([start,end])
        
        return res
    
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]: #Find intersection between 2 lists of intervals
        res=[]
        
        while len(firstList)>0 and len(secondList)>0:
            start,end=firstList[0]
            if end<secondList[0][0]:
                firstList.pop(0)
                continue
            if secondList[0][1]<start:
                secondList.pop(0)
                continue
            
            if len(secondList)>0:
                new_start=max(start,secondList[0][0])
                new_end=min(end,secondList[0][1])
                res.append([new_start,new_end])
                if new_end<end:
                    secondList.pop(0)
                else:
                    firstList.pop(0)
                    
        return res 
                
def Heap():
    def maxHeap():
        minHeap=[-stone for stone in stones]
        heapq.heapify(minHeap)

        while minHeap:
            s1=-heappop(minHeap)
            if not minHeap:
                return s1
            s2=-heappop(minHeap)
            if s1>s2:
                heappush(minHeap,s2-s1)
                
def Trie():
    class TrieNode:
        def __init__(self):
            # self.char=char
            self.children={}
            self.end=False
            
    class Trie:
        def __init__(self):
            self.head=TrieNode()

        def insert(self, word: str) -> None:
            curr=self.head
            for char in word:
                if char not in curr.children:
                    curr.children[char]=TrieNode()
                curr=curr.children[char]
            curr.end=True

        def search(self, word: str) -> bool:
            curr=self.head
            for char in word:
                if char not in curr.children:
                    return False
                curr=curr.children[char]
            return curr.end

        def startsWith(self, prefix: str) -> bool:
            curr=self.head
            for char in prefix:
                if char not in curr.children:
                    return False
                curr=curr.children[char]
            return True
### Course Schedule
def canFinish(self, numCourses: int,prerequisites:List[List[int]]) -> bool:
        # Map each course to its prerequisites
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Store all courses along the current DFS path
        visiting = set()
        def dfs(crs):
            if crs in visiting:
                # Cycle detected
                return False
            if preMap[crs] == []:
                return True
            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

##### Union Find
def findCircleNum(is_connected):
    n = len(is_connected)
    parent = list(range(n))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # Path compression
        return parent[x]
    
    def union(x, y):
        parent[find(x)] = find(y)
    
    for i in range(n):
        for j in range(n):
            if is_connected[i][j]:
                union(i, j)
    
    return len(set(find(i) for i in range(n)))
  
##### Topological Sort
def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        output = []
        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output

#### Kadanes Algo (Maximum Subarray Sum)
def kadanes(nums):
    maxSum=nums[0]
    curSum=nums[0]
    for num in nums[1:]:
        curSum=max(num,curSum+num)
        maxSum=max(maxSum,curSum)
    return maxSum

#Dijkstra Algorithm
def dijkstraShortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        result={}
        for i in range(n):
            result[i]=-1
        result[src]=0

        graph=defaultdict(list)
        for source,dest,wt in edges:
            graph[source].append([dest,wt])

        visited=set()
        minHeap=[[0,src]]
        while minHeap:
            currDist,currNode=heapq.heappop(minHeap)
            if currNode in visited:
                continue
            visited.add(currNode)
            result[currNode]=currDist
            for nextNode,nextWeight in graph[currNode]:
                print(nextNode,nextWeight)
                if nextNode not in visited:
                    heapq.heappush(minHeap,[currDist+nextWeight,nextNode])

        return result

# decorator
def timer(func):
    def wrapper(*args, **kwargs): #add self for method deccorators
        start_time = time.time()  # High-resolution timer
        result = func(*args, **kwargs)    # Execute the decorated function
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer
def square(n):
    return n*n

square(2)

# print("Hello World!")
zeros = [ [0]*len(matrix[0]) for _ in range(len(matrix)) ] #Print 2D array of 0s
print((palindromePartition("abcd")))
# print(allSubStr("brownfox"))