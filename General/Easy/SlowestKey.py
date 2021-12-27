class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        maxKey = keysPressed[0]
        maxDuration = releaseTimes[0]

        for i in range(1, len(releaseTimes)):
            duration = releaseTimes[i] - releaseTimes[i-1]
            if duration > maxDuration:
                maxDuration = duration
                maxKey = keysPressed[i]
            elif duration == maxDuration:
                if maxKey < keysPressed[i]:
                    maxKey = keysPressed[i]

        return maxKey
