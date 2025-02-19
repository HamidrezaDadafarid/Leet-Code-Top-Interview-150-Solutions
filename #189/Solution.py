from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotates the array to the right by k steps.
        
        This is done using the reverse method:
        1. Reverse the entire array.
        2. Reverse the first k elements.
        3. Reverse the remaining elements from index k to the end.
        
        Time Complexity: O(n) - Each reversal operation runs in O(n), and we perform three reversals.
        Space Complexity: O(1) - The rotation is done in place with no extra space used.
        """
        
        def reverse(nums: List[int], start: int, end: int) -> None:
            """
            Helper function to reverse a portion of the list in place.
            """
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]  # Swap elements
                start += 1
                end -= 1

        n = len(nums)
        k = k % n  # Handle cases where k is larger than n

        # Step 1: Reverse the entire array
        reverse(nums, 0, n - 1)
        # Step 2: Reverse the first k elements
        reverse(nums, 0, k - 1)
        # Step 3: Reverse the remaining elements
        reverse(nums, k, n - 1)
