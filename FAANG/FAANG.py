"""1. The HashMap Blueprint(Arrays & Hashing)
Use when: You need to count things, find duplicates, or track seen items.
Space: O(N) | Time: O(N)
"""
def hash_map_pattern(nums):
    # 1. Initialize the HashMap (Dictionary)
    # Key = The number/item, Value = The count or index
    count_map = {}

    for num in nums:
        # A. LOGIC: Check if we have seen this before
        if num in count_map:
            return True  # Or return the pair, index, etc.

        # B. STORAGE: Store it for later
        # We can store 'True', or the index 'i', or increment a counter
        count_map[num] = count_map.get(num, 0) + 1

    return False
"""








2. The Two Pointers Blueprint 
Use when: You have a sorted array and need to find pairs, or you need to reverse / manipulate a string.
Space: $O(1)$ | Time: O(N)
"""

def two_pointers_pattern(nums, target):
    # 1. Initialize pointers at opposite ends
    left = 0
    right = len(nums) - 1

    # 2. Converge them until they touch
    while left < right:
        # Calculate current sum (or logic)
        current_sum = nums[left] + nums[right]

        if current_sum > target:
            right -= 1  # Too big? Decrease logic (Move Right Left)
        elif current_sum < target:
            left += 1  # Too small? Increase logic (Move Left Right)
        else:
            return [left, right]  # Found it!

    return []

"""
3. The Sliding Window Blueprint
Use when: You analyze a continuous
subarray(e.g., "Longest substring," "Max sum of size k").
Space: $O(1)$ or $O(N)$ | Time: O(N)
"""

def sliding_window_pattern(nums):
    # 1. Initialize Window pointers and variables
    left = 0
    current_sum = 0
    max_val = 0

    # 2. Expand the Right pointer (Grow the window)
    for right in range(len(nums)):
        current_sum += nums[right]  # Add new element to window

        # 3. Contract the Left pointer (Shrink window if valid/invalid)
        # WHILE the window is "bad" (e.g. sum is too big), shrink it
        while current_sum > "SOME_LIMIT":
            current_sum -= nums[left]  # Remove left element
            left += 1  # Move left boundary

        # 4. Update Result (Window is now valid)
        # Calculate size: (right - left + 1)
        max_val = max(max_val, right - left + 1)

    return max_val

"""
4. The Tree DFS Blueprint(Recursive)
Use when: You need to explore a Tree(DOM, JSON, Decisions).This 
covers 90 % of "Tree" questions.
Space: $O(H)$ (Height of tree) | Time: O(N)
"""
def dfs_tree_pattern(root):
    # 1. Base Case: If we hit the bottom (null), stop.
    if not root:
        return 0  # Or None, or False

    # 2. Logic for the current node (Pre-order)
    # print(root.val)

    # 3. Recurse (Dive Deeper)
    left = dfs_tree_pattern(root.left)
    right = dfs_tree_pattern(root.right)

    # 4. Return Logic (Post-order) - e.g., max depth
    return 1 + max(left, right)

"""
5. The BFS Blueprint(Graphs & Levels)
Use when: You need "Shortest Path" or "Level-by-Level" analysis.
Space: $O(W)$ (Width of graph) | Time: O(N)
"""
from collections import deque

def bfs_graph_pattern(start_node): # 1. Initialize Queue and Visited Set
    queue = deque([start_node])
    visited = set()
    visited.add(start_node)

    level = 0

    while queue:
        # Process current level size (Snapshot of current layer)
        for i in range(len(queue)):
            node = queue.popleft()  # Get next node

            # A. Process Node
            if node == "TARGET":
                return level

            # B. Add Neighbors
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

        # Finished a layer, move to next
        level += 1
    return -1

"""
6. The Heap Blueprint(Top K Elements)
Use when: You need the "Top 10" or "Smallest 5" items dynamically.
Space: O(K) | Time: O(N \logK)
"""
import heapq
def top_k_elements_pattern(nums, k):
    # 1. Initialize Heap
    min_heap = []

    for num in nums:
        # 2. Push item to heap
        heapq.heappush(min_heap, num)

        # 3. Maintain size K
        # If heap is too big, remove the smallest item
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    # 4. Result is the heap (The K largest items)
    return min_heap