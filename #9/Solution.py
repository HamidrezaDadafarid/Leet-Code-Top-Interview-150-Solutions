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
        return str(x) == str(x)[::-1]

    # Time complexity: O(n), where n is the number of digits in x.
    # Space complexity: O(n) due to the storage of the string and its reverse.

    def isPalindrome3(self, x: int) -> bool:
        # Convert the number to a string and get its length.
        x = str(x)
        n = len(x)

        # Check if the number is negative by looking at the first character.
        if x[0] == "-":
            return False

        # Compare digits from the start and end moving towards the center.
        for i in range(n // 2):
            if x[i] != x[n - i - 1]:
                return False

        # If all pairs matched, it's a palindrome.
        return True

    # Time complexity: O(n), where n is the number of digits in x.
    # Space complexity: O(1) for the iteration but O(n) due to the string conversion.

    def isPalindrome4(self, x: int) -> bool:
        # If the number is negative or if it ends with a 0 (and is not 0 itself),
        # it cannot be a palindrome.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            # Move the last digit of x to reversed_half.
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # x == reversed_half when the number has an even number of digits.
        # x == reversed_half // 10 when the number has an odd number of digits.
        return x == reversed_half or x == reversed_half // 10

    # Time complexity: O(log10(x)) because we process half of the digits.
    # Space complexity: O(1) since we are only using a few variables.
