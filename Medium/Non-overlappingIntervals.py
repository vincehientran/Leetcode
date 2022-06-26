class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals = sorted(intervals)

        noOverlap = [intervals[0]]

        for interval in intervals[1:]:
            if noOverlap[-1][1] > interval[0]:
                noOverlap[-1] = [noOverlap[-1][0], min(noOverlap[-1][1], interval[1])]
            else:
                noOverlap.append(interval)

        return len(intervals) - len(noOverlap)
