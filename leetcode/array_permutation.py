class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[value] for index, value in enumerate(nums)]