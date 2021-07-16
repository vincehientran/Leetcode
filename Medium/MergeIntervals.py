class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals)

        result = [intervals[0]]

        for interval in intervals[1:]:
            if result[-1][1] >= interval[0]:
                result[-1] = [result[-1][0], max(result[-1][1], interval[1])]
            else:
                result.append(interval)


        return result
