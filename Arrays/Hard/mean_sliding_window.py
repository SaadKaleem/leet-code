"""
13/05/2022 - https://leetcode.com/problems/sliding-window-median/

Runtime: 6679 ms, faster than 9.31% of Python3 online submissions for Sliding Window Median.
Memory Usage: 15.8 MB, less than 74.00% of Python3 online submissions for Sliding Window Median.
"""
from typing import List 

"""
For n elements in the list
Time complexity: O(n)
Space complexity: O(num of sub arrays which is equivalent to length of the array)
"""

"""
Further Resources:

https://docs.python.org/3/library/bisect.html

"""

#Pure Array-Based Solution - Not the best, in terms of Runtime though.

class Solution:
    
    def find_median(self, arr_list):
        arr_list.sort() #How long does native sorting take? Time Complexity?
        mid = len(arr_list) // 2
        return (arr_list[mid] + arr_list[~mid]) / 2
    
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if k == len(nums):
            return [self.find_median(nums)]
        else:
            window_num = 0
            
            output_arr = []
            
            while k + window_num <= len(nums):
                sub_array = nums[window_num:k+window_num]
                
                output_arr.append(self.find_median(sub_array))
                
                window_num += 1
                
            return output_arr
