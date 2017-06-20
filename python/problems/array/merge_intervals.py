# Given a collection of intervals, merge all overlapping intervals.

# For example:

# Given [1,3],[2,6],[8,10],[15,18],

# return [1,6],[8,10],[15,18].

# Make sure the returned intervals are sorted.


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        if not intervals:
            return None
        intervals.sort(key=lambda interval: interval.start)
                
        curr_interval = intervals[0]
        i = 1
        while i < len(intervals):
            interval = intervals[i]
            if curr_interval.end < interval.start or interval.end < curr_interval.start:
                curr_interval = intervals[i]
                i += 1
            else:
                curr_interval.end = max(curr_interval.end, interval.end)
                intervals.pop(i)
            
        return intervals
    