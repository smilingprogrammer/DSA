class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        max_distance = float('-inf')
        heaters.sort()
        
        for h in houses:

            left = 0
            right = len(heaters) - 1

            while left < right:

                mid = ( left + right ) // 2

                if heaters[mid] >= h:
                    right = mid

                else:
                    left = mid + 1

            # left distance

            dist1 = abs(h - heaters[left])

            # prev
            dist2 = abs(h - heaters[left - 1]) if left > 0 else float('inf')

            min_dist = min(dist1, dist2)

            max_distance = max(min_dist, max_distance)

        
        return max_distance