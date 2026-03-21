class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = float('inf')

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            lo, hi = i + 1, n - 1

            while lo < hi:

            # closest = 0
            # for i in range(len(nums) - 2):
                curr_sum = nums[i] + nums[lo] + nums[hi]

                if abs(curr_sum - target) < abs(closest - target):
                    closest = curr_sum
                
                if curr_sum == target:
                    return curr_sum
                elif curr_sum < target:
                    lo += 1

                else:
                    hi -= 1

            # diff = target - curr_sum
            # if diff < closest:
            #     closest = curr_sum
        
        return closest