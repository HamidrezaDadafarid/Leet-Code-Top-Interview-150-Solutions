from typing import List


class Solution:
    # Single Pass:
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        # Create an empty dictionary to store the indices of the elements
        hashmap = {}

        # Iterate through the list once
        for i in range(len(nums)):
            # Calculate the complement of the current element
            complement = target - nums[i]

            # Check if the complement exists in the hashmap
            if complement in hashmap:
                # If the complement is found, return the indices
                return [hashmap[complement], i]

            # Store the index of the current element in the hashmap
            hashmap[nums[i]] = i

        # If no solution is found, return an empty list
        return []

    # Time Complexity: O(n)
    # The algorithm makes a single pass over the list of nums, so the time complexity is O(n).

    # Space Complexity: O(n)
    # The hashmap stores each element of the input list once, leading to an O(n) space complexity.

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        # Create an empty dictionary to store the indices of the elements
        hashmap = {}

        # First pass: populate the hashmap with the elements and their indices
        for i in range(len(nums)):
            hashmap[nums[i]] = i

        # Second pass: find the two indices that sum up to the target
        for i in range(len(nums)):
            # Calculate the complement of the current element
            complement = target - nums[i]

            # Check if the complement exists in the hashmap and is not the same element
            if complement in hashmap and i != hashmap[complement]:
                return [i, hashmap[complement]]

        # If no solution is found, return an empty list
        return []

    # Time Complexity: O(n)
    # The algorithm makes two passes over the list of nums:
    # 1. O(n) to populate the hashmap.
    # 2. O(n) to find the two indices that sum up to the target.
    # Hence, the overall time complexity is O(n).

    # Space Complexity: O(n)
    # The hashmap stores each element of the input list once, leading to an O(n) space complexity.
