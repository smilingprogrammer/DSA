class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # return [x for x in nums if x != val]
        l = 0
        while l < len(nums):
            if nums[l] == val:
                nums.remove(nums[l])
            else:
                l += 1

        return len(nums)