"""
06/05/2022 - https://leetcode.com/problems/set-matrix-zeroes/

Accepted Solution at 236ms run-time and 14.9 MB MB memory usage - ~16% better than most python solutions.
"""

from typing import List

"""
The challenge is to replace the zeros in the 2D Matrix in-place with minimal space complexity.

For m rows, and n columns:
Time complexity: O((m*n*(m + n)) + m*n)
Space complexity: O(1)
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #traverse the rows first
        for idx_r in range(0, len(matrix)):
            for idx_c in range(0, len(matrix[0])):
                if matrix[idx_r][idx_c] == 0:
                    col_idx_zero = idx_c
                    #Set all the columns in this row, to be -1.1, except at any idx where it's 0
                    for idx in range(0, len(matrix[0])):
                        if idx_c != idx and matrix[idx_r][idx] == 0:
                            continue
                        else:
                            matrix[idx_r][idx] = -1.1
                    
                    #Zero found in this row, at idx_c
                    #For all rows, at idx_c, set them as -1.1 if the row isn't a zero
                    for idx in range(0, len(matrix)):
                        if idx_r != idx and matrix[idx][idx_c] == 0:
                            continue
                        else:
                            matrix[idx][idx_c] = -1.1
        
        for idx_r in range(0, len(matrix)):
            for idx_c in range(0, len(matrix[0])):
                if matrix[idx_r][idx_c] == -1.1:
                    matrix[idx_r][idx_c] = 0
                    
        return matrix