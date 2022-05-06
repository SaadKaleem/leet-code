"""
06/05/2022 - https://leetcode.com/problems/majority-element/

Runtime: 208 ms, faster than 55.50% of Python3 online submissions for Majority Element.
Memory Usage: 15.4 MB, less than 87.29% of Python3 online submissions for Majority Element.
"""

from typing import List 

"""
For m elements in the list
Time complexity: O(m)
Space complexity: O(num of unique elements)
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}
        
        for element in nums:
            if not hash_map.get(element, None):
                hash_map[element] = 1
            else:
                hash_map[element] += 1
                
                if (hash_map[element] / len(nums)) > 0.5:
                    return element
        
        for key, count in hash_map.items():
            if (count / len(nums)) > 0.5:
                return key