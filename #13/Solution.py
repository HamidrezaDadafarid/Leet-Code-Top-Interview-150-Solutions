class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Converts a Roman numeral string to an integer.

        Explanation:
        1. HashMap Storage: Stores the integer values for each Roman numeral.
        2. Iterate Through String:
           - If the current numeral is smaller than the next, subtract it (e.g., IV -> 4, where I (1) is subtracted).
           - Otherwise, add its value.
        3. Last Character Handling: Since the loop stops at n - 1, the last character’s value is always added separately.

        Time Complexity: O(n) - We iterate through the string once.
        Space Complexity: O(1) - We use a fixed-size hashmap.
        """

        # Dictionary to store the integer values of Roman numerals
        hashmap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        result = 0
        n = len(s)

        # Iterate through the string except the last character
        for i in range(n - 1):
            # If the current value is less than the next, subtract it
            if hashmap[s[i]] < hashmap[s[i + 1]]:
                result -= hashmap[s[i]]
            else:
                result += hashmap[s[i]]

        # Add the value of the last character
        result += hashmap[s[n - 1]]

        return result
