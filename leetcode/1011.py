class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max (weights)
        high = sum(weights)
        max_capacity = high
        def canCarry(capacity):
        # this func return if it's possible
        # to carry all the packages within
        #n days at this capacity
            currCapicaty = capacity
            curr_ships = 1
            for w in weights:
                if currCapicaty - w < 0:
                    curr_ships += 1
                    currCapicaty = capacity
                currCapicaty -= w
            return curr_ships <= days

        while low <= high:
            mid = (low + high)//2
            if canCarry(mid):
                high = mid - 1
                max_capacity = min(max_capacity, mid)
            else:
                low = mid + 1
                
        return max_capacity