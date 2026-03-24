class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 2:
            return n

        left = 0
        max_len = 1

        for right in range(1, n):
            if arr[right] == arr[right - 1]:

                left = right
            elif right >= 2 and (arr[right] > arr[right-1]) == (arr[right-1] > arr[right-2]):

                left = right - 1

            max_len = max(max_len, right - left + 1)

        return max_len