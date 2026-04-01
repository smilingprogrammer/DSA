class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def at_most(distinct_limit: int) -> int:
            left = 0
            freq = defaultdict(int)
            distinct_count = 0
            total = 0

            for right in range(len(nums)):
                if freq[nums[right]] == 0:
                    distinct_count += 1
                freq[nums[right]] += 1

                while distinct_count > distinct_limit:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        distinct_count -= 1
                    left += 1

                total += right - left + 1

            return total

        return at_most(k) - at_most(k - 1)