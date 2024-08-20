class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Create a dictionary to store the frequency of each letter in the magazine.
        dic = {}
        for letter in magazine:
            # Increment the count of each letter
            dic[letter] = dic.get(letter, 0) + 1

        # Check if each letter in the ransomNote can be constructed from the magazine.
        for letter in ransomNote:
            if not letter in dic:  # If the letter is not in the dictionary, return False
                return False
            dic[letter] -= 1  # Decrement the count for the letter in the dictionary

        # After decrementing, check if any letter has a negative count.
        # A negative count would indicate that the ransom note requires more instances of that letter
        # than what the magazine provides.
        for value in dic.values():
            if value < 0:
                return False  # If any count is negative, return False

        # If all checks pass, the ransom note can be constructed from the magazine.
        return True


"""
Time Complexity:
- The time complexity is O(m + n), where m is the length of the magazine string 
  and n is the length of the ransomNote string. This is because we iterate over 
  each character in both the magazine and ransomNote exactly once.

Space Complexity:
- The space complexity is O(1) in the best case, and O(k) in the worst case, 
  where k is the number of distinct characters in the magazine. This is because 
  the size of the dictionary depends on the number of distinct characters, 
  which is limited by the number of characters in the input alphabet (usually 26 for lowercase English letters).
"""
