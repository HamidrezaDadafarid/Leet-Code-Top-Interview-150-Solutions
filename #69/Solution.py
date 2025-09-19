class Solution:
    def mySqrt1(self, x: int) -> int:
        for i in range(x + 1):
            if i * i > x:
                return i - 1

        return x

    # time complexity: O(sqrt(x))
    # space complexity: O(1)

    def mySqrt2(self, x: int) -> int:
        left, right = 0, x
        result = 0

        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
                result = mid
            else:
                right = mid - 1

        return result

    # time complexity: O(log(x))
    # space complexity: O(1)
