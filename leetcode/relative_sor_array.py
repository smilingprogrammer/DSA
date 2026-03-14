class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        count = [0] * 1001

        for num in arr1:
            count[num] += 1

        result = []

        for num in arr2:
            result.extend([num] * count[num])
            count[num] = 0

        for num in range(1001):
            if count[num]:
                result.extend([num] * count[num])

        return result