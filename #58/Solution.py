class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Returns the length of the last word in a given string.

        Time Complexity: O(n)
        The loop iterates through the string once in reverse, where n is the length of the string.
        In the worst case, it will check every character in the string, leading to O(n) time complexity.

        Space Complexity: O(1)
        The algorithm uses only a constant amount of extra space for variables like last_word_length and i.
        Thus, the space complexity is O(1).
        """

        last_word_length = 0
        n = len(s)

        for i in range(n - 1, -1, -1):
            if s[i] == " " and last_word_length != 0:
                break
            elif s[i] == " ":
                continue
            else:
                last_word_length += 1

        return last_word_length

    def lengthOfLastWord2(self, s: str) -> int:
        """
        Returns the length of the last word in a given string.

        Explanation:
        1. Initialize `last_word_length = 0` to store the length of the last word.
        2. Skip trailing spaces by iterating backward from the last character (`i = n - 1`).
        3. Count the length of the last word by continuing until a space is found.
        4. Return the length of the last word once counting stops.

        Time Complexity: O(n) - In the worst case, we iterate through the entire string once.
        Space Complexity: O(1) - We use a few integer variables but no additional data structures.
        """

        last_word_length = 0
        n = len(s)

        # Step 1: Skip trailing spaces
        i = n - 1
        while i >= 0 and s[i] == " ":
            i -= 1

        # Step 2: Count the length of the last word
        while i >= 0 and s[i] != " ":
            last_word_length += 1
            i -= 1

        # Step 3: Return the result
        return last_word_length
