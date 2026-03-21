class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        
        odd_count = 0
        result = 0
        
        for num in nums:
            odd_count += num % 2
            result += prefix_count[odd_count - k]
            prefix_count[odd_count] += 1
        
        return result