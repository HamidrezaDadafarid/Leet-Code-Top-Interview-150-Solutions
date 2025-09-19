class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Check if the input list is empty; if so, return 0
        if not nums:
            return 0

        # `w` is the write pointer; it keeps track of where to place unique or allowed elements
        # `count` keeps track of how many times a number has appeared consecutively
        w = 1  # start from index 1 because index 0 is always kept
        count = 1  # initially, the first number is counted once

        # Loop through the array starting from index 1
        for r in range(1, len(nums)):
            if (
                nums[r] == nums[r - 1]
            ):  # if the current element is the same as the previous one
                count += 1  # increment the count of consecutive duplicates
            else:
                count = 1  # reset count when a new number is encountered

            # If the count is less than or equal to 2, keep the current element
            if count <= 2:
                nums[w] = nums[r]  # place the current element at the `w` pointer
                w += 1  # move the write pointer to the next position

        # Return the new length of the array with allowed duplicates (at most 2 duplicates)
        return w


# Time Complexity:
# O(n) where n is the number of elements in the input list `nums`.
# The algorithm iterates through the list once with a single loop.

# Space Complexity:
# O(1) because the solution uses a constant amount of extra space,
# only modifying the list in place without using any additional data structures.
