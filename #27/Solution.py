class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Initialize a counter `k` that will track the number of elements
        # that are not equal to `val`.
        k = 0

        # Iterate over each element in the array `nums`.
        for i in range(len(nums)):
            # If the current element is not equal to `val`,
            # copy it to the position at index `k` and increment `k`.
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        # After the loop, `k` will be the new length of the array
        # containing elements that are not equal to `val`.
        return k

# Time Complexity: O(n), where `n` is the length of the array `nums`.
# The function iterates through each element in `nums` exactly once.

# Space Complexity: O(1), since the algorithm modifies the input array `nums` in place
# and uses only a constant amount of extra space for the variable `k`.
