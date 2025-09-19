from collections import Counter
from typing import List

class Solution:
    # This method uses a hashmap (Counter) to count the occurrences of each element in the list. It then iterates through the hash map to find and return the element that appears exactly once.
    # Time Complexity = O(n), Space Complexity = O(n)
    def singleNumber1(self, nums: List[int]) -> int:
        hashmap = Counter(nums)
        for x in hashmap:
            if hashmap[x] == 1:
                return x
         
    # The best approach to achieve this is by using the bitwise XOR operator. The XOR operator has a few key properties that make it very useful for this problem:
    # 1. a ⊕ a = 0 for any integer a.
    # 2. a ⊕ 0 = a for any integer a.
    # 3. XOR is commutative and associative, meaning the order of operations doesn't matter.
    # Given these properties, if we XOR all the elements in the array, the elements that appear twice will cancel each other out (since a ⊕ a = 0), and we will be left with the single element that appears only once.
    # Time Complexity = O(n), Space Complexity = O(1)        
    def singleNumber2(self, nums: List[int]) -> int:
        result = 0
        for x in nums:
            result ^= x
        return result
        