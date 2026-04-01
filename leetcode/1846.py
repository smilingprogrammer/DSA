class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        
        arr.sort()
        arr[0] = 1
        
        for i in range(1, len(arr)):

            adj_diff = abs(arr[i] - arr[i - 1])
            if adj_diff > 1:
                arr[i] = abs(adj_diff - arr[i]) + 1

        
        return max(arr)