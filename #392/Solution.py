class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Determines if string 's' is a subsequence of string 't'.

        A subsequence means 's' appears in 't' in the same order but not necessarily consecutively.

        Time Complexity: O(n), where n is the length of 't'.
        - We traverse 't' once while maintaining a pointer for 's'.
        - Each comparison operation is O(1), leading to an overall O(n) complexity.

        Space Complexity: O(1)
        - We use only a few integer variables (i, j) and no additional data structures.
        - Space usage remains constant regardless of input size.

        :param s: The subsequence candidate.
        :param t: The string in which we check for the subsequence.
        :return: True if 's' is a subsequence of 't', otherwise False.
        """
        i = 0  # Pointer for 's'

        for j in range(len(t)):  # Iterate through 't'
            if i < len(s) and t[j] == s[i]:  # If characters match, move pointer 'i'
                i += 1

        return i == len(s)  # If 'i' reached the end of 's', then 's' is a subsequence
