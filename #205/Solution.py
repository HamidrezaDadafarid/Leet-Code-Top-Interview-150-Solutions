class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Initialize two hashmaps (dictionaries) to store character mappings
        hashmap_s_to_t = {}
        hashmap_t_to_s = {}

        # Iterate through each character in the strings `s` and `t` using their indices
        for i in range(len(s)):
            # Check if the mapping in either hashmap is inconsistent with the current characters
            # in `s` and `t`
            if (s[i] in hashmap_s_to_t and hashmap_s_to_t[s[i]] != t[i]) or \
               (t[i] in hashmap_t_to_s and hashmap_t_to_s[t[i]] != s[i]):
                return False
            
            # Establish a mapping from the character in `s` to the corresponding character in `t`
            hashmap_s_to_t[s[i]] = t[i]
            # Establish a mapping from the character in `t` to the corresponding character in `s`
            hashmap_t_to_s[t[i]] = s[i]

        # If all character mappings are consistent, the strings are isomorphic
        return True

# Time Complexity: O(n), where n is the length of the string `s` (or `t`, since both have the same length).
# The loop iterates through each character of the strings once, and dictionary operations (insertions and lookups) are O(1).

# Space Complexity: O(1) in terms of the size of the English alphabet, as the dictionaries will have at most 26 keys.
# However, in general, it is O(n) considering all possible characters, as each character in the strings could be unique.
