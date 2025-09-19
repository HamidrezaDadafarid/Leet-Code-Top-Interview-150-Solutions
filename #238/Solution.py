class Solution:
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        for i in range(n):
            for j in range(n):
                if j == i:
                    continue
                result[i] *= nums[j]

        return result

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        n = len(nums)

        result = [0] * n

        prefix = [0] * n
        postfix = [0] * n

        for i in range(n):
            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = prefix[i - 1] * nums[i]

        for i in range(n - 1, -1, -1):
            if i == n - 1:
                postfix[i] = nums[i]
            else:
                postfix[i] = postfix[i + 1] * nums[i]

        for i in range(n):
            if i == 0:
                result[i] = postfix[i + 1]
            elif i == n - 1:
                result[i] = prefix[i - 1]
            else:
                result[i] = prefix[i - 1] * postfix[i + 1]

        return result
