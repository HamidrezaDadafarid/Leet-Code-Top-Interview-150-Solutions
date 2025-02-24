class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Helper function to check if a character is alphanumeric
        def isAlNum(char: str) -> bool:
            return ("a" <= char <= "z") or ("A" <= char <= "Z") or ("0" <= char <= "9")

        # Helper function to convert an uppercase letter to lowercase
        def lower(char: str) -> str:
            result = ""
            if "A" <= char <= "Z":  # If it's an uppercase letter
                result = chr(
                    ord(char) + 32
                )  # Convert to lowercase using ASCII manipulation
            else:
                result = char  # If it's already lowercase or a digit, return as is
            return result

        # Initialize two pointers: one at the beginning and one at the end of the string
        i, j = 0, len(s) - 1

        while i < j:
            # Move the left pointer if it's not an alphanumeric character
            if not isAlNum(s[i]):
                i += 1
                continue

            # Move the right pointer if it's not an alphanumeric character
            if not isAlNum(s[j]):
                j -= 1
                continue

            # Compare lowercase versions of the characters
            if lower(s[i]) == lower(s[j]):
                i += 1
                j -= 1  # Move both pointers inward if they match
            else:
                return False  # If they don't match, it's not a palindrome

        return True  # If we exit the loop, it's a palindrome


"""
Time Complexity:
- O(N), where N is the length of the input string.
- Each character is processed at most once (moving left and right pointers), leading to a linear scan.

Space Complexity:
- O(1), since only a few extra variables (i, j) and helper functions are used, without additional data structures.
"""
