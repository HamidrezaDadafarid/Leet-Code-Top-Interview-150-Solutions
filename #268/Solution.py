from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Get the length of the input list
        n = len(nums)

        # Calculate the expected sum of numbers from 0 to n using the formula n * (n + 1) // 2
        expected_sum = n * (n + 1) // 2

        # Calculate the actual sum of the numbers in the list
        real_sum = sum(nums)

        # The missing number is the difference between the expected sum and the real sum
        return expected_sum - real_sum

        # Time Complexity: O(n) - we iterate through the list once to calculate the sum
        # Space Complexity: O(1) - we use a constant amount of extra space
