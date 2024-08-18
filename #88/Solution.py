from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merge two sorted arrays nums1 and nums2 into nums1 as one sorted array in-place.

        Args:
        nums1 (List[int]): The first sorted array with m elements followed by n empty spaces for merging.
        m (int): The number of actual elements in nums1.
        nums2 (List[int]): The second sorted array with n elements.
        n (int): The number of elements in nums2.

        Returns:
        None: Modifies nums1 in-place to become the merged sorted array.
        """

        # Pointers for nums1, nums2, and the merged array
        x, y, z = m - 1, n - 1, (m + n) - 1

        # Merge nums1 and nums2 starting from the end to the beginning
        while x >= 0 and y >= 0:
            if nums1[x] > nums2[y]:
                # If the current element in nums1 is greater, place it in the correct position
                nums1[z] = nums1[x]
                x -= 1
            else:
                # If the current element in nums2 is greater or equal, place it in the correct position
                nums1[z] = nums2[y]
                y -= 1
            z -= 1

        # If there are any remaining elements in nums2, copy them over to nums1
        while y >= 0:
            nums1[z] = nums2[y]
            y -= 1
            z -= 1

        # Note: No need to copy elements from nums1 because they are already in place.

# Time Complexity: O(m + n)
# The algorithm iterates over both arrays once, resulting in a linear time complexity.

# Space Complexity: O(1)
# The merging is done in-place in nums1, so no additional space is used beyond the input parameters.
