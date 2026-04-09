class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = [-1] * n

        stack = []

        for i in range(2 * n):
            while stack and nums[stack[-1]] < nums[i % n]:
                idx = stack.pop()
                ans[idx] = nums[i % n]

            if i < n:
                stack.append(i)

        return ans
        # maximum = max(nums)

        # for i in range(len(nums)):
        #     if nums[i] == maximum:
        #         nums[i] = -1
        #     else:
        #         nums[i] += 1
            

        return nums