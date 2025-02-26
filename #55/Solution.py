class Solution:

    # Recursive Solution
    # Time Complexity: O(max(nums) ^ 2)
    # Space Complexity: O(n)
    def canJump1(self, nums: List[int]) -> bool:
        n = len(nums)

        def can_reach(i):
            if i == n - 1:
                return True

            for jump in range(1, numq[i] + 1):
                if can_reach(i + jump):
                    return True

            return False

        return can_reach(0)

    # Greedy Approach (Start At End)
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def canJump2(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n - 1

        for i in range(n - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0

    # Top Down DP (Memorization)
    # Time Complexity: O(n ^ 2)
    # Space Complexity: O(n)
    def canJump3(self, nums: List[int]) -> bool:
        n = len(nums)
        mem = {n - 1: True}

        def can_reach(i):
            if i in mem:
                return mem[i]

            for jump in range(1, numq[i] + 1):
                if can_reach(i + jump):
                    mem[i] = True
                    return True

            mem[i] = False
            return False

        return can_reach(0)
