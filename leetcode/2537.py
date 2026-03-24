class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        pairs = 0
        left = 0
        count = 0

        for right in range(len(nums)):

            pairs += freq[nums[right]]
            freq[nums[right]] += 1

            while pairs >= k:
                freq[nums[left]] -= 1
                pairs -= freq[nums[left]]
                left += 1

            count += left

        return count