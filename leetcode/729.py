class MyCalendar:

    def __init__(self):
        self.calendar = []
        

    def book(self, startTime: int, endTime: int) -> bool:
        # self.array.append([startTime, endTime])

        # right, left = 0, len(self.array) - 1
        # i = 0
        # for i in range(len(self.array)):

        #     if self.array:
        #         if startTime >= self.array[i][0] or endTime < self.array[i][0]:
        #             return False
        #     # while left <= right:
        #     #     middle = (left + right) // 2

        #     #     if startimeself.array[i][0]

        # return True
        left, right = 0, len(self.calendar) - 1
        idx = len(self.calendar)

        while left <= right:
            mid = (left + right) // 2
            if self.calendar[mid][0] < startTime:
                left = mid + 1
            else:
                idx = mid
                right = mid - 1

        if idx < len(self.calendar) and self.calendar[idx][0] < endTime:
            return False

        if idx > 0 and self.calendar[idx - 1][1] > startTime:
            return False

        self.calendar.insert(idx, (startTime, endTime))
        return True

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)