class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        # print(range(length))
        # for n in range(nums[0], nums[-1]):
        for n in range(len(nums) + 1):
            if n not in nums:
                return n