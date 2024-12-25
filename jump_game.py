class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # exhaustive approach using bfs approach where we can see repeated subproblems when all the options from a choice are explored
        q = deque([0])
        n = len(nums)
        if n == 1:
            return True
        visited = set()
        visited.add(0)

        while q:
            curr_idx = q.popleft()

            for next_idx in range(curr_idx + 1, curr_idx + nums[curr_idx] + 1):
                if next_idx >= n - 1:
                    return True
                if next_idx not in visited:
                    q.append(next_idx)
                    visited.add(next_idx)
        return False
        # time complexity is O(n^2)
        # space complexity is O(n)

        # greedy method
        farthest = 0
        n = len(nums)

        for i in range(n):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
            if farthest >= n - 1:
                return True
        return False
