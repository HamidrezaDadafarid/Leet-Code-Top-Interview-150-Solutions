class Solution:
    def isPalindrome1(self, x: int) -> bool:
        # Check if the number is negative. If it is, it's not a palindrome.
        if x < 0:
            return False

        # Store the original number to compare later.
        original = x
        reversed_num = 0

        # Reverse the number by extracting digits from the end and appending them to reversed_num.
        while x > 0:
            reversed_num = reversed_num * 10 + (x % 10)
            x //= 10

        # Compare the original number with the reversed number.
        return original == reversed_num

    # Time complexity: O(log10(x)) because the number of digits in x is log10(x).
    # Space complexity: O(1) as only a few extra variables are used.

    def isPalindrome2(self, x: int) -> bool:
        # Convert the number to a string and check if it is equal to its reverse.
        s = str(x)
        return s == s[::-1]

    # Time complexity: O(n), where n is the number of digits in x.
    # Space complexity: O(n) due to the storage of the string and its reverse.

    def isPalindrome3(self, x: int) -> bool:
        # Check if the number is negative.
        if x < 0:
            return False

        # Convert the number to a string and get its length.
        x = str(x)
        n = len(x)

        # Compare digits from the start and end moving towards the center.
        for i in range(n // 2):
            if x[i] != x[n - i - 1]:
                return False

        # If all pairs matched, it's a palindrome.
        return True

    # Time complexity: O(n), where n is the number of digits in x.
    # Space complexity: O(1) for the iteration but O(n) due to the string conversion.
