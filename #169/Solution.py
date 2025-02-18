class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}

        # Building the hashmap with counts of each element
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        # Checking for the majority element
        for num in hashmap:
            if hashmap[num] > len(nums) // 2:
                return num

    # Time Complexity: O(N), where N is the number of elements in the array.
    # The first loop runs in O(N) time to build the hashmap.
    # The second loop runs in O(N) time to check for the majority element.
    # Space Complexity: O(N), where N is the number of elements in the array.
    # This is because, in the worst case, we might need to store each element in the hashmap.

    def majorityElement2(self, nums: List[int]) -> int:
        # Initialize the candidate for majority element and a counter
        candidate = None
        count = 0

        # First pass to find the candidate
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1

        # Second pass to confirm the candidate (optional if problem guarantees majority element exists)
        count = 0
        for num in nums:
            if num == candidate:
                count += 1

        if count > len(nums) // 2:
            return candidate

        # If there is no majority element (not required by the problem constraints)
        return -1

    # The Boyer-Moore Voting Algorithm
    # Time Complexity: O(N), where N is the number of elements in the array.
    # Space Complexity: O(1), since we are using only a few extra variables.
