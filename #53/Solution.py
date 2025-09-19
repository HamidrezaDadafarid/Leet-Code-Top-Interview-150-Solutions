class Solution:
    # Time Complexity: O(n^3)
    # The outer loop runs n times.
    # The second loop runs n - i times (in the worst case, roughly n).
    # The innermost loop runs n - i times as well for each (i, j) pair.
    # So in total, the time complexity is O(n^3) because we are iterating through all possible subarrays and summing each of them.

    # Space Complexity: O(1)
    # - The space complexity is constant because we only use a few extra variables (max_sum, s, i, j, k) regardless of the input size.
    def maxSubArray1(self, nums: list[int]) -> int:
        # Initialize max_sum to negative infinity to ensure any sum will be larger.
        max_sum = float("-inf")

        # Outer loop: Iterate over all possible starting points of subarrays.
        for i in range(len(nums)):

            # Second loop: Iterate over all possible ending points of subarrays.
            for j in range(len(nums) - 1, i - 1, -1):

                # Initialize a variable to sum elements of the current subarray.
                current_sum = 0

                # Inner loop: Sum elements from index j to i (inclusive).
                for k in range(j, i - 1, -1):
                    current_sum += nums[k]

                # If the sum of the current subarray is greater than the current max_sum, update max_sum.
                if current_sum > max_sum:
                    max_sum = current_sum

        # Return the maximum sum found.
        return max_sum

    # Time Complexity: O(n^2)
    # The outer loop runs n times (for each starting point).
    # The inner loop runs for roughly n-i times (for each end point starting from i).
    # Therefore, the total time complexity is O(n^2), because we are iterating through all subarrays, but now we reuse the sum for each subarray.

    # Space Complexity: O(1)
    # - The space complexity is constant because we only use a few extra variables (max_sum, current_sum, i, j).
    def maxSubArray2(self, nums: list[int]) -> int:
        # Initialize max_sum to negative infinity to ensure any sum will be larger.
        max_sum = float("-inf")

        # Outer loop: Iterate over all possible starting points of subarrays.
        for i in range(len(nums)):
            # Initialize the current sum for subarrays starting from index i.
            current_sum = 0

            # Inner loop: Iterate over all possible ending points for the subarray starting at i.
            for j in range(i, len(nums)):
                # Add the current element to the current sum.
                current_sum += nums[j]

                # If the current sum is greater than max_sum, update max_sum.
                if current_sum > max_sum:
                    max_sum = current_sum

        # Return the maximum sum found.
        return max_sum

    # Time Complexity: O(n)
    # The algorithm iterates through the list once, performing constant time operations for each element.

    # Space Complexity: O(1)
    # The algorithm uses a fixed amount of extra space (variables cur_sum and max_sum), regardless of the input size.
    def maxSubArray3(self, nums: list[int]) -> int:
        n = len(nums)
        max_sum = float("-inf")
        cur_sum = 0

        # Iterate through the elements of the array.
        for i in range(n):
            # Update cur_sum by comparing the current element and the sum of cur_sum with the current element.
            # This decision point ensures that we either start a new subarray at the current element,
            # or extend the existing subarray to include the current element.
            cur_sum += nums[i]

            # Update global_sum if the current_sum is greater than the global_sum.
            if cur_sum > max_sum:
                max_sum = cur_sum

            if cur_sum <= 0:
                cur_sum = 0

        # Return the largest sum found, which is stored in global_sum.
        return max_sum
