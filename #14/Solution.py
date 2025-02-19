class Solution:
    # Method 1: Sorting the strings and comparing the first and last strings
    def longestCommonPrefix1(self, strs: List[str]) -> str:
        """
        Time Complexity: O(N * log N) due to sorting the strings (where N is the number of strings in the list)
        In the worst case, comparing the first and last string can take O(M) time (where M is the length of the strings)
        Total time complexity: O(N * log N + N * M), which is dominated by the sorting step.

        Space Complexity: O(1) if we don't consider the space used by the input list and result string.
        We only use a few extra variables to store temporary data (like 'first', 'last', 'ans').
        """

        ans = ""

        # Sort the list of strings alphabetically
        strs.sort()

        # After sorting, the common prefix of all strings will be common in the first and last string
        first = strs[0]
        last = strs[len(strs) - 1]

        # Compare the first and last string character by character
        for i in range(1, min(len(first), len(last)) + 1):
            if first[:i] != last[:i]:
                return ans  # Return the common prefix found so far

            ans += first[i - 1]  # Append the common character to ans

        return ans  # Return the final common prefix

    # Method 2: Iteratively comparing each string's prefix
    def longestCommonPrefix2(self, strs: List[str]) -> str:
        """
        Time Complexity: O(N * M) where N is the number of strings and M is the average length of the strings.
        The outer loop runs for the length of the shortest string (O(M)) and the inner loop compares each string (O(N)).
        Total time complexity: O(N * M).

        Space Complexity: O(1) if we don't consider the space used by the input list and result string.
        We only use a few extra variables for temporary storage (like 'min_length', 'prefix', 'ans').
        """

        ans = ""

        # Find the minimum length of strings in the input list
        min_length = len(strs[0])

        for i in range(1, len(strs)):
            # Update the minimum length found so far
            if len(strs[i]) < min_length:
                min_length = len(strs[i])

        if min_length == 0:
            return ""  # If one of the strings is empty, return an empty string

        # Compare the prefix for all strings one character at a time
        for i in range(1, min_length + 1):
            # Take the prefix of length i from the first string
            prefix = strs[0][:i]

            for string in strs[1:]:
                # Compare the current prefix with the other strings
                if string[:i] != prefix:
                    return ans  # Return the common prefix found so far

            ans += prefix[i - 1]  # Append the common character to the result

        return ans  # Return the final common prefix
