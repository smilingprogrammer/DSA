class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        

        output = []
        start =[]
        for i in range(len(intervals)):
            start.append([intervals[i][0], i])

        start = sorted(start)

        print(start)

        for x, y in intervals:

            end = y

            left, right = 0, len(start) - 1

            while left < right:

                mid = (left + right) // 2

                if start[mid][0] >= end:
                    right = mid

                else:
                    left = mid + 1

            next_interval = start[left][1] if start[left][0] >= end else -1

            output.append(next_interval)

        return output