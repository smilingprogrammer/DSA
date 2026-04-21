class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        n = len(nums)
        left, right = 0, n - 1
        ans = 0

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] <= nums[n - 1]:
                ans = middle
                right = middle - 1
            else:
                left = middle + 1

        return nums[ans]