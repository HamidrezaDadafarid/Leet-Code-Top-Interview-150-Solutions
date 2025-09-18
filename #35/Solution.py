class Solution:
    def searchInsert1(self, nums: list[int], target: int) -> int:
        n = len(nums)

        for i in range(n):
            if nums[i] >= target:
                return i

        return n

    # time complexity: O(n) that n is the number of elements in the input array
    # space complexity: O(1)

    def searchInsert2(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left

    # time complexity: O(log(n)) that n is the number of elements in the input array
    # space complexity: O(1)
