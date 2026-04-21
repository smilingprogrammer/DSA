class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        # first position
        def fisrtposition():
            low, high = 0, n-1
            while low <= high:
                mid = (low + high)//2
                if nums [mid] == target:
                    if mid == 0 or nums [mid-1] != target:
                        return mid
                    else:
                        high = mid - 1
                elif nums [mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1
        # last position
        def lastPosition():
            low, high = 0, n-1
            while low <= high:
                mid = (low + high)//2
                if nums [mid] == target:
                    if mid == n-1 or nums [mid+1] != target:
                        return mid
                    else:
                        low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1

        first = fisrtposition()
        last = lastPosition()
        return [first, last]