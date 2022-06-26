class MyCalendar(object):

    def __init__(self):
        self.calendar = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        # find a spot and insert the booking
        prevBooking = None
        for i, booking in enumerate(self.calendar):
            s, e = booking
            
            if s >= end:
                if prevBooking == None:
                    self.calendar.insert(0, (start, end))
                    return True
                elif prevBooking[1] <= start:
                    self.calendar.insert(i, (start, end))
                    return True
                else:
                    return False

            prevBooking = booking

        # if the booking was not added yet
        if len(self.calendar) == 0 or self.calendar[-1][1] <= start:
            self.calendar.append((start, end))
            return True
        else:
            return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
