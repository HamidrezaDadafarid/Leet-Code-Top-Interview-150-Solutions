from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merges two sorted arrays nums1 and nums2 into a single sorted array in-place.
        
        :param nums1: List[int] - First sorted array with enough space at the end to hold nums2.
        :param m: int - Number of initialized elements in nums1.
        :param nums2: List[int] - Second sorted array.
        :param n: int - Number of initialized elements in nums2.
        
        Time Complexity: O(m + n) - Each element from nums1 and nums2 is processed once.
        Space Complexity: O(1) - The merge is done in-place, requiring no extra space.
        """
        
        # Pointers to the last initialized elements of nums1 and nums2
        i, j = m - 1, n - 1
        # Pointer to the last position in nums1
        p = m + n - 1

        # Traverse from the back of both arrays to merge them in descending order
        while p >= 0:
            if i < 0:  # If nums1 is exhausted, copy remaining elements from nums2
                nums1[p] = nums2[j]
                j -= 1

            elif j < 0:  # If nums2 is exhausted, nums1 is already in place
                nums1[p] = nums1[i]
                i -= 1

            else:
                # Compare the last elements of both arrays and place the larger one at nums1[p]
                if nums1[i] < nums2[j]:
                    nums1[p] = nums2[j]
                    j -= 1
                else:
                    nums1[p] = nums1[i]
                    i -= 1

            p -= 1
