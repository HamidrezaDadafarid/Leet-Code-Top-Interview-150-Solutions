class Solution:
    # Time Complexity: O(n * m), where n is the length of haystack and m is the length of needle.
    # Space complexity: O(1), since only a few variables are used.
    def strStr1(self, haystack: str, needle: str) -> int:
        # Get the lengths of haystack and needle
        n = len(haystack)
        m = len(needle)

        # Check if needle is empty string
        if m == 0:
            return 0
        # Check if haystack is empty string
        elif n == 0:
            return -1

        # Iterate through the haystack
        for i in range(n):  # Takes O(n)
            # Check if the substring from i to i+m is within the bounds of haystack
            if (j := i + m) > n:
                break
            # If the substring from i to i+m matches the needle, return the starting index
            elif haystack[i:j] == needle:  # takes O(m)
                return i

        # If no match is found, return -1
        return -1

    # The second one is as same is the first one but the first one is more efficient. the second one has redundant checks.
    # Time Complexity: O(n * m), where n is the length of haystack and m is the length of needle.
    # Space complexity: O(1), since only a few variables are used and no extra space is allocated.
    def strStr2(self, haystack: str, needle: str) -> int:
        # Get the lengths of haystack and needle
        n = len(haystack)
        m = len(needle)

        # Check if needle is empty string
        if m == 0:
            return 0
        # Check if haystack is empty string
        elif n == 0:
            return -1

        # Iterate through each starting position in haystack
        for i in range(n):  # Takes O(n)
            # Iterate through potential substrings of length m
            for j in range(i, n - m + 1):
                # If the substring matches the needle, return the starting index
                if haystack[i : i + m] == needle:  # Takes O(m)
                    return i

        # If no match is found, return -1
        return -1
