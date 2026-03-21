class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        prefix_sum = {0: -1}
        running_sum = 0

        for i, num in enumerate(nums):
            running_sum += num
            remainder = running_sum % k

            if remainder in prefix_sum:
                if  i - prefix_sum[remainder] > 1:
                    return True
            else:
                prefix_sum[remainder] = i

        return False