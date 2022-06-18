"""
19/06/2022 - https://leetcode.com/problems/product-of-array-except-self/

Runtime: 259 ms, faster than 78.59% of Python3 online submissions for Product of Array Except Self.
Memory Usage: 22.3 MB, less than 27.30% of Python3 online submissions for Product of Array Except Self.
"""

from typing import List 

"""
For n items, 
Time complexity: O(n) - 3 iterations
Space complexity: O(n) - 3 lists
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left_product = [1] * len(nums)
        for i in range(0, len(nums)-1):
            left_product[i+1] = nums[i] * left_product[i]
        
        right_product = [1] * len(nums)
        for i in range(len(nums)-1, 0, -1):
            right_product[i-1] = nums[i] * right_product[i]

        answer = []
        for x, y in zip(left_product, right_product):
            answer.append(x * y)

        return answer

if __name__ == "__main__":
    Solution().productExceptSelf([1, 2, 3, 4])