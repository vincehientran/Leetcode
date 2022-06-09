class Logger(object):

    def __init__(self):
        self.timestamps = {}
        

    def shouldPrintMessage(self, timestamp, message):
        """
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message in self.timestamps:
            if timestamp - self.timestamps[message] >= 10:
                self.timestamps[message] = timestamp
                return True
            else:
                return False
        else:
            self.timestamps[message] = timestamp
            return True
        
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)