"""
11/06/2022 - https://leetcode.com/problems/two-sum/submissions/

Runtime: 71 ms, faster than 79.34% of Python3 online submissions for Two Sum.
Memory Usage: 15.2 MB, less than 49.04% of Python3 online submissions for Two Sum.
"""

from typing import List 

"""
For n elements in the list
Time complexity: O(n) -> (Two iterations) - Iteration over the hash map once, and then over the nums list.
Space complexity: O(num of unique elements)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        
        #Populating hash map
        for idx, num in enumerate(nums):
            hash_map[num] = idx
            
        #Now iterating the nums list.
        for idx in range(len(nums)):
            complement = target - nums[idx]
            
            if complement in hash_map: 
                #Moreover, the current idx must not be the same as the one in the hash_map
                if idx != hash_map[complement]:
                    return [idx, hash_map[complement]]
                