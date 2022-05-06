"""
06/05/2022 - https://leetcode.com/problems/pascals-triangle/

Accepted Solution at 32ms run-time and 13.9 MB memory usage - ~86% better than most python solutions.
"""

import math
from typing import List 

"""
For m rows, and n columns:
Time complexity: O(m*n)
Space complexity: O(m*n) since we're returning a 2D array.
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascals_list = []
        for iter_count in range(0, numRows):
            temp_list = []
            for k in range(iter_count):
                """
                Pascal Rule: (n choose k) = C(n, k) = nCk = n!/(k!(n - k)!) 

                https://en.wikipedia.org/wiki/Pascal%27s_rule for Algebraic Proof
                """
                element = int(math.factorial(iter_count) / (math.factorial(k) * math.factorial(iter_count - k)))       
                temp_list.append(element)
            
            temp_list.append(1)

            pascals_list.append(temp_list)
        
        return pascals_list
        