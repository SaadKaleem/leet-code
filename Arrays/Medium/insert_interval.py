"""
19/06/2022 - https://leetcode.com/problems/insert-interval/

Runtime: 82 ms, faster than 95.25% of Python3 online submissions for Insert Interval.
Memory Usage: 17.6 MB, less than 16.57% of Python3 online submissions for Insert Interval.
"""

from typing import List

"""

For n intervals:
Time complexity: O(n) - 1 pass over the list of intervals.
Space complexity: O(n) - 2 lists, to keep track of left and right sub-intervals
"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = [], []

        newIntervalStart, newIntervalEnd = newInterval[0], newInterval[1]

        for interval in intervals:

            # represents the start and end of each interval
            intervalStart = interval[0] 
            intervalEnd = interval[1]

            # if end of the interval is lesser than the start of our newInterval, we will just append this to our `left`
            if intervalEnd < newIntervalStart:
                left += [interval]
            # if start of the interval is greater than the end of our newInterval, we will just append this to our `right`
            elif intervalStart > newIntervalEnd:
                right += [interval]
            # Else, we need to combine this interval
            else:
                newIntervalStart = min(intervalStart, newIntervalStart)
                newIntervalEnd = max(intervalEnd, newIntervalEnd)

        return left + [[newIntervalStart, newIntervalEnd]] + right

if __name__ == "__main__":
    sol = Solution().insert([[1,5],[6,8]], [0,5])
    print(sol)