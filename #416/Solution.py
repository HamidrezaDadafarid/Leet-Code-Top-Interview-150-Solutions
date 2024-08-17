class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Calculate the total sum of the array
        total_sum = sum(nums)

        # If the total sum is odd, we cannot partition the array into two equal subsets
        if total_sum % 2 != 0:
            return False

        # Target sum for each subset (half of the total sum)
        target = total_sum // 2

        # Initialize a 2D DP array where dp[i][j] represents whether we can achieve sum 'j'
        # using the first 'i' numbers.
        dp = [[False] * (target + 1) for _ in range(len(nums) + 1)]

        # It's always possible to achieve a sum of 0 (by selecting no elements)
        for i in range(len(dp)):
            dp[i][0] = True

        # Initialize the first row of the DP table
        # (If we have no numbers, we cannot achieve any positive sum)
        for i in range(1, target + 1):
            dp[0][i] = False

        # Fill the DP table
        for i in range(1, len(dp)):
            for j in range(1, target + 1):
                if nums[i - 1] > j:  # If the current number is greater than the sum we're targeting
                    # Can't include this number, so take the value from the previous row
                    dp[i][j] = dp[i - 1][j]
                else:
                    # Otherwise, we check if we can either:
                    # 1. Achieve the sum 'j' without the current number (dp[i-1][j])
                    # 2. Achieve the sum 'j' by including the current number (dp[i-1][j-nums[i-1]])
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

        # The result will be whether we can achieve 'target' sum using all numbers
        return dp[-1][-1]

# Time Complexity:
# The time complexity of this algorithm is O(n * target), where `n` is the number of elements in `nums`
# and `target` is half of the total sum. This is because we fill a DP table of size (n+1) x (target+1).

# Space Complexity:
# The space complexity is also O(n * target) due to the space required to store the DP table.
