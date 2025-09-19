class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # Initialize two pointers, L at the beginning and R at the end of the list
        L = 0
        R = len(nums) - 1
        # Initialize an empty list to store the results
        result = []

        # Iterate while the left pointer is less than or equal to the right pointer
        while L <= R:
            # Compare the absolute values of the elements at the left and right pointers
            if abs(nums[L]) > abs(nums[R]):
                # If the left element's absolute value is greater, append its square to the result
                result.append(nums[L] ** 2)
                # Move the left pointer to the right
                L += 1
            else:
                # If the right element's absolute value is greater or equal, append its square to the result
                result.append(nums[R] ** 2)
                # Move the right pointer to the left
                R -= 1

        # The result list contains the squares in non-increasing order, reverse it to get non-decreasing order
        return result[::-1]

    # Time Complexity: O(n)
    # The algorithm iterates through the list once, so the time complexity is O(n).

    # Space Complexity: O(n)
    # The result list stores n elements, leading to an O(n) space complexity.
