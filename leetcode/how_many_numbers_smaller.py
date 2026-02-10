class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        num_to_count = {}
        
        for i, num in enumerate(sorted_nums):
            if num not in num_to_count:
                num_to_count[num] = i
        
        return [num_to_count[num] for num in nums]