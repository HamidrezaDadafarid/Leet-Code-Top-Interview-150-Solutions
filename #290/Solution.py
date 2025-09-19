class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Split the input string into a list of words
        words = s.split(" ")

        # If the number of characters in the pattern and the number of words do not match, return False
        if len(pattern) != len(words):
            return False
        
        # Create two hash maps to establish a bijection between pattern characters and words
        charToWord, wordToChar = {}, {}

        # Iterate over the pattern and words simultaneously
        for i in range(len(pattern)):
            # If the character has already been mapped, check if it maps to the same word
            if (pattern[i] in charToWord and words[i] != charToWord[pattern[i]]):
                return False
            # If the word has already been mapped, check if it maps to the same character
            if (words[i] in wordToChar and pattern[i] != wordToChar[words[i]]):
                return False

            # Establish the bidirectional mapping between character and word
            charToWord[pattern[i]] = words[i]
            wordToChar[words[i]] = pattern[i]
        
        # If all checks pass, return True
        return True

    """
    Time Complexity: O(n)
    - We iterate over the pattern and words once (O(n)), where n is the length of the pattern (or words).
    - Dictionary operations (insertion and lookup) take O(1) on average, so the overall complexity remains O(n).
    
    Space Complexity: O(n)
    - We store mappings for each unique character and word in two dictionaries.
    - In the worst case, all characters and words are unique, leading to O(n) space usage.
    """