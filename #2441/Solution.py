from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        # Initialize an empty set to keep track of the numbers we have seen
        seen = set()
        # Initialize the answer to -1, which is returned if no valid k is found
        ans = -1

        # Iterate through each number in the input list
        for num in nums:
            # Check if the absolute value of num is greater than the current answer
            # and if the opposite sign of num has already been seen
            if abs(num) > ans and -num in seen:
                # Update the answer to the absolute value of num
                ans = abs(num)
            else:
                # Add the current number to the set of seen numbers
                seen.add(num)

        # Return the maximum k found or -1 if no such k exists
        return ans

    # Time Complexity: O(n)
    # The algorithm iterates through the list of nums once, making the time complexity O(n).

    # Space Complexity: O(n)
    # The set `seen` can store up to n elements in the worst case, leading to an O(n) space complexity.
