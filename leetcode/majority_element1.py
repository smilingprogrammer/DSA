class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_nums = Counter(nums)

        most_count = 0
        most_key = 0

        for key, value in count_nums.items():
            if value > most_count:
                most_count = value
                most_key = key

        return most_key