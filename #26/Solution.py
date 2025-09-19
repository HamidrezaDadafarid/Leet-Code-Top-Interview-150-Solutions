class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Initialize pointer p to 1, which keeps track of the position
        # where the next unique element should be placed.
        p = 1

        # Initialize last_unique_element to the first element of the array.
        last_unique_element = nums[0]

        # Iterate over the array starting from the second element.
        for i in range(1, len(nums)):
            if nums[i] != last_unique_element:
                # If the current element is different from the last unique element,
                # place it at the p-th position in the array.
                nums[p] = nums[i]

                # Update last_unique_element to the current element.
                last_unique_element = nums[i]

                # Increment the pointer p.
                p += 1

        # Return the length of the modified array, which is represented by p.
        return p


# Time Complexity: O(n)
# The code iterates through the list once, so the time complexity is O(n), where n is the length of the array.

# Space Complexity: O(1)
# The algorithm uses only a few extra variables (p and last_unique_element), so the space complexity is O(1).
