class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # sort
        # then replace the duplicates with _
        # nums.sort()
        # for i in range(len(nums) - 1):
        #     if nums[i] == nums[i+1]:
        #         nums[i], nums[i + 1] = nums[i + 1], None
        # print(nums)
        i = 0
        ## Replace with nums[i] with j
        for j in nums:
            if i == 0 or j != nums[i - 1]:
                nums[i] = j
                i += 1
        # print(nums)

        return i

        # nums.pop(0)
        # return [x for x in nums if x != None]
        # for i in range(len(nums) - 1):
        #     if nums[i] > nums[i+1]:
        #         nums[i], nums[i + 1] = nums[i + 1], nums [i]