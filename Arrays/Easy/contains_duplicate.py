"""
06/05/2022 - https://leetcode.com/problems/contains-duplicate/

Runtime: 625 ms, faster than 46.27% of Python3 online submissions for Contains Duplicate.
Memory Usage: 26 MB, less than 71.56% of Python3 online submissions for Contains Duplicate
"""

from typing import List 

"""
For n elements in the list
Time complexity: O(1)
Space complexity: O(n)
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return True if len(set(nums)) != len(nums) else False 
        